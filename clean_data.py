import pandas as pd
import os


# --------------------------------------------------
# 1. File paths
# --------------------------------------------------

INPUT_FILE = "data/survey.csv"
OUTPUT_FILE = "data/survey_cleaned.csv"


# --------------------------------------------------
# 2. Load dataset
# --------------------------------------------------

print("Loading dataset...")

df = pd.read_csv(INPUT_FILE)

print("Original shape:", df.shape)


# --------------------------------------------------
# 3. Clean column names
# --------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^\w]+", "_", regex=True)
    .str.strip("_")
)


# --------------------------------------------------
# 4. Remove duplicate rows
# --------------------------------------------------

before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

print("Duplicates removed:", before_duplicates - after_duplicates)


# --------------------------------------------------
# 5. Replace common missing-value indicators
# --------------------------------------------------

missing_values = [
    "",
    " ",
    "na",
    "n/a",
    "N/A",
    "NA",
    "null",
    "NULL",
    "?",
    "unknown",
    "Unknown"
]

df = df.replace(missing_values, pd.NA)


# --------------------------------------------------
# 6. Remove completely empty columns
# --------------------------------------------------

df = df.dropna(axis=1, how="all")


# --------------------------------------------------
# 7. Clean text columns
# --------------------------------------------------

text_columns = df.select_dtypes(include=["object"]).columns

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()


# --------------------------------------------------
# 8. Fill missing values
# --------------------------------------------------

for column in df.columns:

    if pd.api.types.is_numeric_dtype(df[column]):
        df[column] = df[column].fillna(df[column].median())

    else:
        mode = df[column].mode(dropna=True)

        if not mode.empty:
            df[column] = df[column].fillna(mode[0])


# --------------------------------------------------
# 9. Create data directory if it doesn't exist
# --------------------------------------------------

os.makedirs("data", exist_ok=True)


# --------------------------------------------------
# 10. Save cleaned dataset
# --------------------------------------------------

df.to_csv(OUTPUT_FILE, index=False)

print("Cleaning completed!")
print("Cleaned shape:", df.shape)
print(f"Cleaned dataset saved to: {OUTPUT_FILE}")