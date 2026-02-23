# ============================================
# 1. Task Description
# Remove duplicate rows from a DataFrame to obtain unique store/type
# combinations, unique store/department combinations, and unique holiday
# dates. The goal is to avoid counting repeated records and extract
# meaningful unique entries from the sales dataset.
#
# 2. Topics Covered
# - Dropping duplicates with .drop_duplicates()
# - Subsetting columns to define uniqueness
# - Filtering rows before removing duplicates
# - Selecting specific columns for output
# ============================================

# 3. Python Script

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"] == True].drop_duplicates(subset=["date"])

# Print date col of holiday_dates
print(holiday_dates["date"])

===========
# 4. Additional Notes
# Dropping duplicates
# Removing duplicates is key to obtaining accurate counts and avoiding
# repeated observations. The .drop_duplicates() method allows you to
# specify which columns define a "duplicate."
#
# Examples:
# - Unique store/type pairs reveal the set of store formats.
# - Unique store/department pairs show which departments exist in each store.
# - Filtering rows before dropping duplicates (e.g., is_holiday == True)
#   helps isolate unique dates for specific conditions.
#
# Context:
# The DataFrame `sales` is available and pandas has been imported as pd.
# ============================================
