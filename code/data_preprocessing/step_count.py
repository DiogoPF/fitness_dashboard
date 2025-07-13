import pandas as pd

pd.set_option("display.max_columns", None)
df = pd.read_csv(
    r"C:\Users\Diogo\Downloads\com.samsung.shealth.tracker.pedometer_day_summary.20250615023939.csv",
    usecols=["step_count", "update_time", "distance", "calorie"],
    index_col=False,
    skiprows=1,
)


df["update_time"] = pd.to_datetime(df["update_time"]).dt.normalize()

df = df.loc[df.groupby("update_time")["step_count"].idxmax()]
df["distance"] = (df["distance"] / 1000).round(2)
df["calorie"] = (df["calorie"]).round(0).astype(int)

print(df.head())
