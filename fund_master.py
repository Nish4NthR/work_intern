import pandas as pd

df = pd.read_csv("data/raw/1788499983024-b042c300-01_fund_master.csv")

print("COLUMNS:")
print(df.columns.tolist())

print("\nFUND MASTER SHAPE:")
print(df.shape)

print("\nFUND HOUSES:")
print(df["fund_house"].unique())

print("\nCATEGORIES:")
print(df["category"].unique())

print("\nSUB CATEGORIES:")
print(df["sub_category"].unique())

print("\nPLANS:")
print(df["plan"].unique())

print("\nRISK CATEGORIES:")
print(df["risk_category"].unique())

print("\nBENCHMARKS:")
print(df["benchmark"].unique())

print("\nFUND MANAGERS:")
print(df["fund_manager"].unique())

print("\nSCHEME CODES:")
print(df["amfi_code"].head(20))

print("\nEXPENSE RATIOS:")
print(df["expense_ratio_pct"].describe())

print("\nEXIT LOAD:")
print(df["exit_load_pct"].describe())

print("\nMINIMUM SIP AMOUNTS:")
print(df["min_sip_amount"].describe())

print("\nMINIMUM LUMPSUM AMOUNTS:")
print(df["min_lumpsum_amount"].describe())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

print("\nFIRST 5 RECORDS:")
print(df.head())