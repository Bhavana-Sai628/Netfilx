import pandas as pd
import kagglehub
import os

# Download dataset
df = pd.read_csv("netflix_titles.csv")

# Drop duplicates and missing values
df.drop_duplicates(inplace=True)
df.dropna(subset=['title', 'type'], inplace=True)

# Standardize column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Convert date columns
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Save cleaned data
df.to_csv(os.path.join("cleaned_netflix_titles.csv"), index=False)