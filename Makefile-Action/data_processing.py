import sys
import pandas as pd
from pathlib import Path

#output_path = Path("/home/sarrj/mdp_load_sos/load_sos/Makefile-Action/processed_data")
#output_path.mkdir(parents=True, exist_ok=True)

# Check if the data location argument is provided
if len(sys.argv) != 2:
    print("Usage: python data_processing.py <dta_location>")
    sys.exit(1)

# Load the raw dataset (step 1)
df = pd.read_csv(sys.argv[1])

# Rename columns to more descriptive name (step2)

df.columns = [
    "Country",
    "Happiness Score",
    "Happiness Score Error",
    "Upper Whisker",
    "Lower Whisker",
    "GDP per Capita",
    "Social Support",
    "Healthy Life Expectancy",
    "Freedom to Make Life Choices",
    "Generosity",
    "Perceptions of Corruption",
    "Dystopia Happiness Score",
    "GDP per Capita",
    "Social Support",
    "Healthy Life Expectancy",
    "Freedom to Make Life Choices",
    "Generosity",
    "Perceptions of Corruption",
    "Dystopia Residual",
]

# Handle missing values by replacing them with the mean (step 3)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Check for missing values after cleaning
print("Missing values after cleaning:")
print(df.isnull().sum())

print(df.head())

# Save the cleaned and normalized dataset to a new CSV file (step 4)
df.to_csv("WHR2023_cleaned.csv", index=False)
#df.to_csv(output_path / "WHR2023_cleaned.csv", index=False)
