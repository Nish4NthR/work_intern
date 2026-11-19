
import requests
import pandas as pd
from pathlib import Path
import time

# Output directory
OUTPUT_DIR = Path("data/raw/live_nav")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Required mutual fund schemes
SCHEMES = {
    "HDFC_Top_100_Direct": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

BASE_URL = "https://api.mfapi.in/mf/"

def fetch_nav(name, scheme_code):

    url = BASE_URL + scheme_code

    print(f"\nFetching {name} ({scheme_code})")

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        result = response.json()

        # Extract scheme metadata
        metadata = result.get("meta", {})

        # Extract NAV history
        nav_data = result.get("data", [])

        if not nav_data:
            print("No NAV records returned.")
            return

        df = pd.DataFrame(nav_data)

        df["scheme_code"] = scheme_code
        df["scheme_name"] = metadata.get(
            "scheme_name", name
        )

        # Convert data types
        df["date"] = pd.to_datetime(
            df["date"],
            format="%d-%m-%Y",
            errors="coerce"
        )

        df["nav"] = pd.to_numeric(
            df["nav"],
            errors="coerce"
        )

        # Save raw NAV data
        output_file = OUTPUT_DIR / f"{name}_{scheme_code}.csv"

        df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")
        print(f"Records: {len(df)}")
        print(f"Scheme: {metadata.get('scheme_name', name)}")

    except requests.RequestException as e:
        print(f"API request failed: {e}")

    except (ValueError, KeyError) as e:
        print(f"Data processing error: {e}")


if __name__ == "__main__":

    for name, code in SCHEMES.items():
        fetch_nav(name, code)
        time.sleep(1)

    print("\nNAV FETCHING COMPLETED")
