import pandas as pd

pd.set_option("display.max_columns", None)
df = pd.read_csv(r"C:\Users\Diogo\Downloads\hellohabit_habit_activity.csv")

# Convert to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%y")

# Group by month without creating a new column
monthly = df.groupby(df["Date"].dt.to_period("W")).sum(numeric_only=True)
monthly = monthly.astype(int)
print(monthly)
