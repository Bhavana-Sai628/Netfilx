1. Import Required Libraries
import pandas as pd
import kagglehub
import os
pandas: For data manipulation and analysis.

kagglehub: Included but not used in this script — can be removed unless you plan to download from Kaggle through code.

os: Used for file handling and constructing file paths.

2. Load Dataset
df = pd.read_csv("netflix_titles.csv")
Loads the original dataset into a Pandas DataFrame.

This dataset contains information about Netflix titles, including name, genre, release year, country, and more.

3. Clean the Data

df.drop_duplicates(inplace=True)
df.dropna(subset=['title', 'type'], inplace=True)
Removes duplicate rows to avoid redundancy.

Drops rows that are missing crucial information such as title or type (e.g., movie or TV show).

4. Standardize Column Names

df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
Converts column names to lowercase.

Removes any leading/trailing whitespace.

Replaces spaces with underscores (_) for better accessibility and readability in code.

5. Convert Date Columns

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
Converts the date_added column to a proper datetime format.

errors='coerce' ensures any non-date values are replaced with NaT (missing datetime).

6. Save the Cleaned Dataset

df.to_csv(os.path.join("cleaned_netflix_titles.csv"), index=False)
Exports the cleaned DataFrame to a new CSV file named cleaned_netflix_titles.csv.

index=False ensures the row index is not saved as a column.

