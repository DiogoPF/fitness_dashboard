import pandas as pd

pd.set_option("display.max_columns", None)
df = pd.read_csv(
    r"C:\Users\Diogo\Downloads\strong7219039073999397906.csv", sep=";", index_col=False
)


# Create exercise order per workout
df["Exercise Order"] = df.groupby("Workout #")["Exercise Name"].transform(
    lambda x: pd.factorize(x)[0] + 1
)

print(df.head())
# lst_exercices = df["Exercise Name"].unique().tolist()
# print(lst_exercices)


# import json

# with open(r"C:\Users\Diogo\Downloads\exercises.json") as f:
#     data = json.load(f)
# exer = [item for item in data if item.get("name") == "Lateral "]
# print(exer)
