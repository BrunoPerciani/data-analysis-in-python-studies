# ============================================
# 1. Task Description
# Identify missing values in a dataset of plane ticket prices, determine
# whether each column exceeds a 5% missing‑data threshold, and drop rows
# with missing values only in columns that fall below the threshold.
#
# 2. Topics Covered
# - Counting missing values with .isna().sum()
# - Calculating percentage-based thresholds
# - Using Boolean masks to select columns
# - Dropping missing values with .dropna()
# ============================================

# 3. Python Script

# Count the number of missing values in each column
print(planes.isna().sum())

# Find the five percent threshold
threshold = len(planes) * 0.05

# Create a filter
cols_to_drop = planes.columns[planes.isna().sum() <= threshold]

# Drop missing values for columns below the threshold
planes.dropna(subset=cols_to_drop, inplace=True)

print(planes.isna().sum())

# ============================================
# 4. Additional Notes
# Dealing with missing data
# - A common approach is to drop missing values when they represent a
#   small fraction of the dataset (here, ≤ 5%).
# - planes.isna().sum() returns the number of missing entries per column.
# - Columns with missing counts below the threshold are included in
#   cols_to_drop, and .dropna(subset=...) removes rows missing values
#   only in those selected columns.
#
# Caveat:
# - inplace=True modifies the original DataFrame directly; use with care
#   or replace with planes = planes.dropna(...).
#
# Context:
# pandas is imported as pd.
# The DataFrame `planes` contains plane ticket price information.
# ============================================
