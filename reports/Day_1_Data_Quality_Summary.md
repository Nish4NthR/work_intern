# Day 1 – Data Quality Summary

**Project:** Mutual Fund Analytics  
**Scope:** CSV ingestion, initial data-quality checks, Fund Master exploration, AMFI code validation, and live NAV API integration.

## 1. Dataset Overview

| Dataset | Records | Columns |
|---|---:|---:|
| Investor transactions | 32,778 | 13 |
| Portfolio holdings | 322 | 8 |
| Benchmark indices | 8,050 | 3 |
| Fund master | 40 | 15 |
| NAV history | 46,000 | 3 |
| AUM by fund house | 90 | 5 |
| Monthly SIP inflows | 48 | 6 |
| Category inflows | 144 | 3 |
| Industry folio count | 21 | 6 |
| Scheme performance | 40 | 19 |
| **Total** | **87,533** | **81** |

## 2. Data Quality Findings

- **Missing values:** 12, all in `yoy_growth_pct` in `monthly_sip_inflows.csv`.
- **Duplicate rows:** 0 reported across all 10 datasets.
- **Data types:** Numeric fields were identified as integer or float. Date-like fields are stored as strings and should be converted to date/period types before analysis.
- **Invalid dates:** Not separately checked in the supplied inspection output.
- **Other observations:** Validate numeric ranges, portfolio weight totals, and cross-dataset relationships in the next quality-check stage.

## 3. Live NAV API Integration

**API:** [https://api.mfapi.in](https://api.mfapi.in)

| Requested scheme | Code | Records fetched | API-reported scheme |
|---|---:|---:|---|
| HDFC Top 100 Direct | 125497 | 3,209 | SBI Small Cap Fund – Direct Plan – Growth |
| SBI Bluechip | 119551 | 3,352 | Aditya Birla Sun Life Banking & PSU Debt Fund – Direct Plan – IDCW-Re-investment |
| ICICI Bluechip | 120503 | 3,424 | Axis ELSS Tax Saver Fund – Direct Plan – Growth Option |
| Nippon Large Cap | 118632 | 3,415 | Nippon India Large Cap Fund – Direct Plan – Growth Option |
| Axis Bluechip | 119092 | 3,681 | HDFC Money Market Fund – Direct Plan – Growth Option |
| Kotak Bluechip | 120841 | 3,418 | Quant Mid Cap Fund – Direct Plan – Growth Option |
| **Total** | **6 requests** | **20,499** | |

- API requests completed and six CSV files were saved.
- The returned scheme name matches the requested scheme for **1 of 6** requests.
- **5 scheme-name mismatches** require investigation before using these files for scheme-level analysis.

## 4. Fund Master Exploration

**Fund Master size:** 40 records × 15 columns

| Attribute | Unique values |
|---|---:|
| Fund houses | 10 |
| Categories | 2 |
| Sub-categories | 12 |
| Risk categories | 5 |
| Plans | 2 |
| Benchmarks | 10 |
| Fund managers | 29 |

- Categories: Equity, Debt.
- Plans: Regular, Direct.
- Risk categories: Moderate, Very High, Low, High, Moderately High.
- Missing values: 0.
- Duplicate rows: 0.

## 5. AMFI Code Validation

| Check | Result |
|---|---:|
| Total Fund Master codes | 40 |
| Total NAV codes | 40 |
| Valid codes | 40 |
| Missing codes | 0 |
| Duplicate Fund Master codes | 0 |

**Status:** All 40 Fund Master codes were matched in the NAV-code validation output.

## 6. Conclusion

The 10 datasets contain **87,533 records**. Initial checks reported **no duplicate rows** and **12 missing values**, all in the monthly SIP growth field. The Fund Master has no reported missing values or duplicate rows, and AMFI code validation passed for all 40 codes.

The main issue is the live NAV integration: five of the six API responses returned scheme names that do not match the requested schemes. Verify the scheme-code mappings and correct the fetch process before using those NAV files.

**Next actions**
1. Investigate and correct the five live NAV scheme-code mismatches.
2. Convert date-like columns and validate date values.
3. Review the 12 missing SIP growth values.
4. Check numeric ranges, portfolio weights, and cross-dataset consistency.
