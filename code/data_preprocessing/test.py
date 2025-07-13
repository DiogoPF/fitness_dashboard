import pandas as pd
from datetime import date

pd.set_option("display.max_columns", None)

# Load and prepare data
df = pd.read_csv(
    "../data/body_composition.csv",
    header=None,
    names=[
        "date",
        "skeletal_muscle_mass",
        "body_fat_mass",
        "body_fat_percentage",
        "weight",
    ],
)
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

# Set index to week number
weekly = weekly.set_index("week_number")
weekly = weekly.reset_index()
# Save to CSV
# weekly.to_csv("../data/body_composition_weekly.csv")


iso_calendar = date.today().isocalendar()
current_week_df = weekly[
    (weekly["week_number"] == iso_calendar.week) & (weekly["year"] == iso_calendar.year)
]
