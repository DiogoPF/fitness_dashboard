import streamlit as st
import pandas as pd
import io
import tempfile
from supabase import create_client, Client


def render():
    # Load secrets
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    bucket = st.secrets["supabase"]["bucket"]

    supabase: Client = create_client(url, key)

    # Download the CSV file from Supabase storage
    file_name = "body_composition_agg.csv"
    response = supabase.storage.from_(bucket).download(file_name)

    # Load into pandas
    csv_bytes = response
    df = pd.read_csv(io.BytesIO(csv_bytes))
    st.dataframe(df)

    # Process your data (example: filter rows where BMI > 25)
    if "skeletal_muscle_mass" in df.columns:
        df_processed = df[df["skeletal_muscle_mass"] < 30]
    else:
        df_processed = df

    st.dataframe(df_processed)

    # Save processed DataFrame to a temporary local file
    with tempfile.NamedTemporaryFile(
        mode="w+b", suffix=".csv", delete=False
    ) as tmp_file:
        df_processed.to_csv(tmp_file.name, index=False)
        tmp_file_path = tmp_file.name

    # Read the saved file as bytes for upload
    with open(tmp_file_path, "rb") as f:
        file_bytes = f.read()

    # Upload the file bytes to Supabase storage
    new_file_name = "processed_body_composition.csv"
    storage_path = new_file_name  # or "folder/" + new_file_name if you want a folder

    res = supabase.storage.from_(bucket).upload(storage_path, file_bytes)

    if res:
        st.success(f"Uploaded processed file to: {storage_path}")
    else:
        st.error("Upload failed")
