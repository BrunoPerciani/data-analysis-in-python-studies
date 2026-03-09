# ============================================
# 1. Task Description
# Import the divorce dataset and ensure that all date-related columns are
# correctly parsed as datetime objects during import. This allows proper
# time‑based analysis, such as computing marital duration, examining trends
# over time, and comparing ages at marriage or divorce.
#
# 2. Topics Covered
# - Reading CSV files with pandas.read_csv()
# - Using parse_dates to automatically convert columns to datetime dtype
# - Inspecting column data types with .dtypes
# ============================================

# 3. Python Script

# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv(
    "divorce.csv",
    parse_dates=[
        "divorce_date",
        "dob_man",
        "dob_woman",
        "marriage_date"
    ]
)

print(divorce.dtypes)

# ============================================
# 4. Additional Notes
# Importing DateTime data
# - parse_dates=[...] ensures pandas automatically converts the listed
#   columns from strings (object dtype) to datetime64[ns].
# - Datetime dtypes make it possible to:
#       • Calculate time differences (e.g., marriage duration validation)
#       • Extract year, month, or weekday components
#       • Filter records by specific date ranges
#       • Perform time‑series analysis or plotting
#
# Context:
# pandas has been imported as pd.
# The dataset contains marriage and divorce dates, birthdays, and
# non-date features such as education levels and income.
# ============================================
