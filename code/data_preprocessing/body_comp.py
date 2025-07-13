import os
import google.generativeai as genai
from PIL import Image
import pandas as pd
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import shutil
import pandas as pd
from datetime import date
import time

# Get data from Google Drive and process it with Gemini AI
# ______________________________________________________________________________________________________________

script_dir = os.path.dirname(os.path.abspath(__file__))
credentials_path = os.path.join(
    script_dir, "..", "..", "gdrive_acess_files", "settings.yaml"
)

gauth = GoogleAuth()
gauth.LoadCredentialsFile(credentials_path)
gauth.ServiceAuth()
drive = GoogleDrive(gauth)

folder_id = "1FodFgXbcFu4ognvjGbz7sSA0aaDDE01b"

# Only list non-folder files in the folder (e.g., pngs)
file_list = drive.ListFile(
    {
        "q": f"'{folder_id}' in parents and trashed=false and mimeType != 'application/vnd.google-apps.folder'"
    }
).GetList()

download_folder = os.path.join(script_dir, "data", "temp")
os.makedirs(download_folder, exist_ok=True)

for file in file_list:
    filepath = os.path.join(download_folder, file["title"])
    file.GetContentFile(filepath)

# Get Data from pictures
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
prompt = "Please extract the following information from the image: date, Skeletal Muscle Mass, Body Fat Mass, Body Fat Percentage, and Weight. Return the result as plain text in comma-separated values with the columns: date, skeletal_muscle_mass, body_fat_mass, body_fat_percentage, and weight. In the output, include only the values as numbers. The date in the image is formatted as MM/DD/YYYY—please convert and save it as DD/MM/YYYY instead."


output_path = os.path.join(script_dir, "data", "body_composition_full.csv")
new_rows = []


for file in os.listdir(download_folder):
    filepath = os.path.join(download_folder, file)
    with Image.open(filepath) as img:
        response = model.generate_content([prompt, img])
        lines = response.text.strip()
        new_rows.append(lines)
        time.sleep(2)

with open(output_path, "a") as f:
    for row in new_rows:
        f.write(row + "\n")
shutil.rmtree(download_folder)


# _______________________________________________________________________________________________________________

# Aggregate by week
input_path = os.path.join(script_dir, "data", "body_composition_full.csv")
df = pd.read_csv(input_path)
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")

# Group by week (Monday to Sunday)
grouped = df.groupby(pd.Grouper(key="date", freq="W-SUN"))
weekly = grouped.mean().round(2)

# Count data points per week
weekly["n"] = grouped.size().values

# Adjust index to Monday and add week metadata
weekly.index -= pd.Timedelta(days=6)
weekly["week_start"] = weekly.index
weekly["week_end"] = weekly.index + pd.Timedelta(days=6)
weekly["week_number"] = weekly.index.isocalendar().week
weekly["year"] = weekly.index.isocalendar().year
weekly["month"] = weekly.index.month
weekly = weekly.set_index("week_number")
weekly = weekly.reset_index()


# Save to CSV
output_path = os.path.join(script_dir, "data", "body_composition_agg.csv")
weekly.to_csv(output_path, index=False)
