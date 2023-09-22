import pandas as pd

# Preprocessing the pubmed csv file
# Making sure all the dates have the same format
df = pd.read_csv("pubmed.csv")
df = df.dropna()
df.set_index("id", inplace=True)
df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.strftime("%d/%m/%Y")
# Remove unwanted characters
df["journal"] = df["journal"].str.replace(r"\\x[0-9a-fA-F]+", "", regex=True)
df["title"] = df["title"].str.replace(r"\\x[0-9a-fA-F]+", "", regex=True)
df.to_csv("curated_pubmed.csv")

# Preprocessing the clinical trials csv file


def standardize_date_format(date_str):
    try:
        # Attempt to parse the input date string
        return pd.to_datetime(date_str).strftime("%d/%m/%Y")
    except ValueError:
        return date_str


# Dropping null values and Making sure all the dates have the same format
df = pd.read_csv("clinical_trials.csv")
df = df.dropna()
df.set_index("id", inplace=True)
df["date"] = df["date"].apply(standardize_date_format)
df["scientific_title"] = df["scientific_title"].astype(str)
# Remove leading and trailing whitespace
df["scientific_title"] = df["scientific_title"].str.strip()
# Filter the DataFrame to remove blank strings
df = df[df["scientific_title"] != ""]
# Remove unwanted characters
df["journal"] = df["journal"].str.replace(r"\\x[0-9a-fA-F]+", "", regex=True)
df["scientific_title"] = df["scientific_title"].str.replace(
    r"\\x[0-9a-fA-F]+", "", regex=True
)
df.to_csv("curated_clinical_trials.csv")

# Preprocessing the drugs csv file
df = pd.read_csv("drugs.csv")
# Keep the eligible atccodes
df = df[df["atccode"].apply(lambda x: x[0].isalpha())]
df.set_index("atccode", inplace=True)
df.to_csv("curated_drugs.csv")
