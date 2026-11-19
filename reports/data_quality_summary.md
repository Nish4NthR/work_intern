======================================================================
MUTUAL FUND DATA INGESTION
======================================================================

Total CSV files found: 10

======================================================================
DATASET: 1788499980509-304c1255-08_investor_transactions.csv
======================================================================

1. SHAPE:
(32778, 13)

2. DATA TYPES:
investor_id               str
transaction_date          str
amfi_code               int64
transaction_type          str
amount_inr              int64
state                     str
city                      str
city_tier                 str
age_group                 str
gender                    str
annual_income_lakh    float64
payment_mode              str
kyc_status                str
dtype: object

3. FIRST FIVE RECORDS:
  investor_id transaction_date  amfi_code transaction_type  amount_inr  ... age_group  gender annual_income_lakh payment_mode kyc_status
0   INV003054       2024-01-01     119092              SIP        1834  ...       56+  Female               77.1          UPI   Verified
1   INV002952       2024-01-01     148567       Redemption      392882  ...     18-25    Male                7.1       Cheque   Verified
2   INV003420       2024-01-01     118636              SIP         912  ...     36-45    Male               47.2      Mandate   Verified
3   INV003436       2024-01-01     118634              SIP        1102  ...     36-45  Female               54.4       Cheque    Pending
4   INV004691       2024-01-01     119094          Lumpsum        8682  ...     26-35    Male               14.5  Net Banking    Pending

[5 rows x 13 columns]

4. DATA QUALITY CHECKS:
Missing values:
investor_id           0
transaction_date      0
amfi_code             0
transaction_type      0
amount_inr            0
state                 0
city                  0
city_tier             0
age_group             0
gender                0
annual_income_lakh    0
payment_mode          0
kyc_status            0
dtype: int64

Duplicate rows:
0

Unique values:
investor_id            5000
transaction_date        516
amfi_code                40
transaction_type          3
amount_inr            23822
state                    12
city                     24
city_tier                 2
age_group                 5
gender                    2
annual_income_lakh      804
payment_mode              4
kyc_status                2
dtype: int64

======================================================================
DATASET: 1788499982117-e3d6ab98-09_portfolio_holdings.csv
======================================================================

1. SHAPE:
(322, 8)

2. DATA TYPES:
amfi_code              int64
stock_symbol             str
stock_name               str
sector                   str
weight_pct           float64
market_value_cr      float64
current_price_inr    float64
portfolio_date           str
dtype: object

3. FIRST FIVE RECORDS:
   amfi_code stock_symbol                stock_name       sector  weight_pct  market_value_cr  current_price_inr portfolio_date
0     119551    POWERGRID    Power Grid Corporation    Utilities       13.85           737.09            6011.08     2025-12-31
1     119551     HDFCBANK             HDFC Bank Ltd      Banking       11.19            88.97            1074.65     2025-12-31
2     119551       GRASIM     Grasim Industries Ltd  Diversified        9.90           208.45            5964.59     2025-12-31
3     119551      DRREDDY  Dr. Reddy's Laboratories       Pharma        4.76           161.32            3748.82     2025-12-31
4     119551   ASIANPAINT          Asian Paints Ltd       Paints       10.25           725.90            1321.45     2025-12-31

4. DATA QUALITY CHECKS:
Missing values:
amfi_code            0
stock_symbol         0
stock_name           0
sector               0
weight_pct           0
market_value_cr      0
current_price_inr    0
portfolio_date       0
dtype: int64

Duplicate rows:
0

Unique values:
amfi_code             34
stock_symbol          30
stock_name            30
sector                14
weight_pct           295
market_value_cr      322
current_price_inr    322
portfolio_date         1
dtype: int64

======================================================================
DATASET: 1788499982615-f9647ab2-10_benchmark_indices.csv
======================================================================

1. SHAPE:
(8050, 3)

2. DATA TYPES:
date               str
index_name         str
close_value    float64
dtype: object

3. FIRST FIVE RECORDS:
         date index_name  close_value
0  2022-01-03    NIFTY50     17492.79
1  2022-01-04    NIFTY50     17689.64
2  2022-01-05    NIFTY50     17835.05
3  2022-01-06    NIFTY50     17878.51
4  2022-01-07    NIFTY50     17759.15

4. DATA QUALITY CHECKS:
Missing values:
date           0
index_name     0
close_value    0
dtype: int64

Duplicate rows:
0

Unique values:
date           1150
index_name        7
close_value    8027
dtype: int64

======================================================================
DATASET: 1788499983024-b042c300-01_fund_master.csv
======================================================================

1. SHAPE:
(40, 15)

2. DATA TYPES:
amfi_code               int64
fund_house                str
scheme_name               str
category                  str
sub_category              str
plan                      str
launch_date               str
benchmark                 str
expense_ratio_pct     float64
exit_load_pct         float64
min_sip_amount          int64
min_lumpsum_amount      int64
fund_manager              str
risk_category             str
sebi_category_code        str
dtype: object

3. FIRST FIVE RECORDS:
   amfi_code       fund_house                                   scheme_name  ...   fund_manager risk_category sebi_category_code
0     119551  SBI Mutual Fund     SBI Bluechip Fund - Regular Plan - Growth  ...  Sohini Andani      Moderate               EC01
1     119552  SBI Mutual Fund      SBI Bluechip Fund - Direct Plan - Growth  ...  Sohini Andani      Moderate               EC01
2     119598  SBI Mutual Fund    SBI Small Cap Fund - Regular Plan - Growth  ...  R. Srinivasan     Very High               EC03
3     119599  SBI Mutual Fund     SBI Small Cap Fund - Direct Plan - Growth  ...  R. Srinivasan     Very High               EC03
4     119120  SBI Mutual Fund  SBI Magnum Gilt Fund - Regular Plan - Growth  ...   Dinesh Ahuja           Low               DC02

[5 rows x 15 columns]

4. DATA QUALITY CHECKS:
Missing values:
amfi_code             0
fund_house            0
scheme_name           0
category              0
sub_category          0
plan                  0
launch_date           0
benchmark             0
expense_ratio_pct     0
exit_load_pct         0
min_sip_amount        0
min_lumpsum_amount    0
fund_manager          0
risk_category         0
sebi_category_code    0
dtype: int64

Duplicate rows:
0

Unique values:
amfi_code             40
fund_house            10
scheme_name           40
category               2
sub_category          12
plan                   2
launch_date           34
benchmark             10
expense_ratio_pct     31
exit_load_pct          3
min_sip_amount         1
min_lumpsum_amount     3
fund_manager          29
risk_category          5
sebi_category_code     9
dtype: int64

======================================================================
DATASET: 1788499983331-4389156d-02_nav_history.csv
======================================================================

1. SHAPE:
(46000, 3)

2. DATA TYPES:
amfi_code      int64
date             str
nav          float64
dtype: object

3. FIRST FIVE RECORDS:
   amfi_code        date      nav
0     119551  2022-01-03  54.3856
1     119551  2022-01-04  54.3474
2     119551  2022-01-05  54.6869
3     119551  2022-01-06  55.4550
4     119551  2022-01-07  55.3692

4. DATA QUALITY CHECKS:
Missing values:
amfi_code    0
date         0
nav          0
dtype: int64

Duplicate rows:
0

Unique values:
amfi_code       40
date          1150
nav          45594
dtype: int64

======================================================================
DATASET: 1788499984134-b0cbf625-03_aum_by_fund_house.csv
======================================================================

1. SHAPE:
(90, 5)

2. DATA TYPES:
date                  str
fund_house            str
aum_lakh_crore    float64
aum_crore           int64
num_schemes         int64
dtype: object

3. FIRST FIVE RECORDS:
         date           fund_house  aum_lakh_crore  aum_crore  num_schemes
0  2022-03-31      SBI Mutual Fund            6.05     605000          186
1  2022-03-31  ICICI Prudential MF            4.65     465000          216
2  2022-03-31     HDFC Mutual Fund            4.35     435000          195
3  2022-03-31      Nippon India MF            2.70     270000          177
4  2022-03-31    Kotak Mahindra MF            2.70     270000          168

4. DATA QUALITY CHECKS:
Missing values:
date              0
fund_house        0
aum_lakh_crore    0
aum_crore         0
num_schemes       0
dtype: int64

Duplicate rows:
0

Unique values:
date               9
fund_house        10
aum_lakh_crore    82
aum_crore         82
num_schemes       10
dtype: int64

======================================================================
DATASET: 1788499984405-d702a6c6-04_monthly_sip_inflows.csv
======================================================================

1. SHAPE:
(48, 6)

2. DATA TYPES:
month                            str
sip_inflow_crore               int64
active_sip_accounts_crore    float64
sip_aum_lakh_crore           float64
new_sip_accounts_lakh        float64
yoy_growth_pct               float64
dtype: object

3. FIRST FIVE RECORDS:
     month  sip_inflow_crore  active_sip_accounts_crore  new_sip_accounts_lakh  sip_aum_lakh_crore  yoy_growth_pct
0  2022-01             11517                       4.91                   9.10                4.80             NaN
1  2022-02             11438                       4.93                   8.20                4.85             NaN
2  2022-03             12328                       5.09                  10.50                5.01             NaN
3  2022-04             11863                       5.48                   9.52                5.12             NaN
4  2022-05             12286                       5.55                   8.10                5.15             NaN

4. DATA QUALITY CHECKS:
Missing values:
month                         0
sip_inflow_crore              0
active_sip_accounts_crore     0
new_sip_accounts_lakh         0
sip_aum_lakh_crore            0
yoy_growth_pct               12
dtype: int64

Duplicate rows:
0

Unique values:
month                        48
sip_inflow_crore             45
active_sip_accounts_crore    44
new_sip_accounts_lakh        29
sip_aum_lakh_crore           48
yoy_growth_pct               36
dtype: int64

======================================================================
DATASET: 1788499984721-4b860901-05_category_inflows.csv
======================================================================

1. SHAPE:
(144, 3)

2. DATA TYPES:
month                   str
category                str
net_inflow_crore    float64
dtype: object

3. FIRST FIVE RECORDS:
     month         category  net_inflow_crore
0  2024-04        Large Cap            2413.0
1  2024-04          Mid Cap            3897.0
2  2024-04        Small Cap            3533.0
3  2024-04        Flexi Cap            4947.0
4  2024-04  Large & Mid Cap            4214.0

4. DATA QUALITY CHECKS:
Missing values:
month               0
category            0
net_inflow_crore    0
dtype: int64

Duplicate rows:
0

Unique values:
month                12
category             12
net_inflow_crore    142
dtype: int64

======================================================================
DATASET: 1788499985036-da4a0c4a-06_industry_folio_count.csv
======================================================================

1. SHAPE:
(21, 6)

2. DATA TYPES:
month                      str
total_folios_crore     float64
equity_folios_crore    float64
debt_folios_crore      float64
hybrid_folios_crore    float64
others_folios_crore    float64
dtype: object

3. FIRST FIVE RECORDS:
     month  total_folios_crore  equity_folios_crore  debt_folios_crore  hybrid_folios_crore  others_folios_crore
0  2022-01               13.26                 9.28               1.86                 0.80                 1.33
1  2022-04               13.91                 9.74               1.95                 0.83                 1.39
2  2022-07               13.85                 9.69               1.94                 0.83                 1.38
3  2022-10               14.12                 9.88               1.98                 0.85                 1.41
4  2023-01               14.81                10.37               2.07                 0.89                 1.48

4. DATA QUALITY CHECKS:
Missing values:
month                  0
total_folios_crore     0
equity_folios_crore    0
debt_folios_crore      0
hybrid_folios_crore    0
others_folios_crore    0
dtype: int64

Duplicate rows:
0

Unique values:
month                  21
total_folios_crore     21
equity_folios_crore    21
debt_folios_crore      21
hybrid_folios_crore    20
others_folios_crore    21
dtype: int64

======================================================================
DATASET: 1788499985420-bb134abf-07_scheme_performance.csv
======================================================================

1. SHAPE:
(40, 19)

2. DATA TYPES:
amfi_code               int64
scheme_name               str
fund_house                str
category                  str
plan                      str
return_1yr_pct        float64
return_3yr_pct        float64
return_5yr_pct        float64
benchmark_3yr_pct     float64
alpha                 float64
beta                  float64
sharpe_ratio          float64
sortino_ratio         float64
std_dev_ann_pct       float64
max_drawdown_pct      float64
aum_crore               int64
expense_ratio_pct     float64
morningstar_rating      int64
risk_grade                str
dtype: object

3. FIRST FIVE RECORDS:
   amfi_code                                   scheme_name       fund_house   category  ... aum_crore  expense_ratio_pct  morningstar_rating  risk_grade
0     119551     SBI Bluechip Fund - Regular Plan - Growth  SBI Mutual Fund  Large Cap  ...     14288               1.54                   4    Moderate
1     119552      SBI Bluechip Fund - Direct Plan - Growth  SBI Mutual Fund  Large Cap  ...      1231               0.66                   3    Moderate
2     119598    SBI Small Cap Fund - Regular Plan - Growth  SBI Mutual Fund  Small Cap  ...     19259               1.43                   5   Very High
3     119599     SBI Small Cap Fund - Direct Plan - Growth  SBI Mutual Fund  Small Cap  ...     36061               0.72                   4   Very High
4     119120  SBI Magnum Gilt Fund - Regular Plan - Growth  SBI Mutual Fund       Gilt  ...     24101               0.77                   5         Low

[5 rows x 19 columns]

4. DATA QUALITY CHECKS:
Missing values:
amfi_code             0
scheme_name           0
fund_house            0
category              0
plan                  0
return_1yr_pct        0
return_3yr_pct        0
return_5yr_pct        0
benchmark_3yr_pct     0
alpha                 0
beta                  0
sharpe_ratio          0
sortino_ratio         0
std_dev_ann_pct       0
max_drawdown_pct      0
aum_crore             0
expense_ratio_pct     0
morningstar_rating    0
risk_grade            0
dtype: int64

Duplicate rows:
0

Unique values:
amfi_code             40
scheme_name           40
fund_house            10
category              12
plan                   2
return_1yr_pct        39
return_3yr_pct        40
return_5yr_pct        40
benchmark_3yr_pct     40
alpha                 36
beta                  22
sharpe_ratio          24
sortino_ratio         34
std_dev_ann_pct        9
max_drawdown_pct      39
aum_crore             40
expense_ratio_pct     31
morningstar_rating     3
risk_grade             5
dtype: int64

DATA INGESTION INSPECTION COMPLETED