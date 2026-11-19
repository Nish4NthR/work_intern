import pandas as pd

fund_master = pd.read_csv(
    "data/raw/1788499983024-b042c300-01_fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/1788499983331-4389156d-02_nav_history.csv"
)

# Normalize scheme codes
master_codes = set(
    fund_master["amfi_code"]
    .dropna()
    .astype(str)
    .str.strip()
)

nav_codes = set(
    nav_history["amfi_code"]
    .dropna()
    .astype(str)
    .str.strip()
)

# Compare
valid_codes = master_codes.intersection(nav_codes)

missing_codes = master_codes.difference(nav_codes)

print("TOTAL MASTER CODES:", len(master_codes))
print("TOTAL NAV CODES:", len(nav_codes))
print("VALID CODES:", len(valid_codes))
print("MISSING CODES:", len(missing_codes))

print("\nMISSING SCHEME CODES:")
print(sorted(missing_codes))

# Save missing codes
pd.DataFrame({
    "missing_scheme_code": sorted(missing_codes)
}).to_csv(
    "data/processed/missing_scheme_codes.csv",
    index=False
)

print("\nVALIDATION COMPLETED")