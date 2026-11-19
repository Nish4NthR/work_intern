
import pandas as pd
from pathlib import Path

# Dataset directory
DATA_DIR = Path("data/raw")

# Find all CSV files
csv_files = list(DATA_DIR.glob("*.csv"))

print("=" * 70)
print("MUTUAL FUND DATA INGESTION")
print("=" * 70)

print(f"\nTotal CSV files found: {len(csv_files)}")

if len(csv_files) != 10:
    print("WARNING: Expected 10 CSV datasets.")

for file in csv_files:

    print("\n" + "=" * 70)
    print(f"DATASET: {file.name}")
    print("=" * 70)

    try:
        df = pd.read_csv(file)

        # Dataset dimensions
        print("\n1. SHAPE:")
        print(df.shape)

        # Column data types
        print("\n2. DATA TYPES:")
        print(df.dtypes)

        # First five records
        print("\n3. FIRST FIVE RECORDS:")
        print(df.head())

        # Data quality checks
        print("\n4. DATA QUALITY CHECKS:")

        print("Missing values:")
        print(df.isnull().sum())

        print("\nDuplicate rows:")
        print(df.duplicated().sum())

        print("\nUnique values:")
        print(df.nunique())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")

print("\nDATA INGESTION INSPECTION COMPLETED")
