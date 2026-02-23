# ============================================
# 1. Task Description
# Slice a time series DataFrame by date ranges using both Boolean
# conditions and label-based slicing with .loc[] after setting the date
# as the index. The goal is to subset rows in specific periods.
#
# 2. Topics Covered
# - Boolean subsetting on date columns
# - Setting a DateTime index and sorting it
# - Slicing time series with .loc['start':'end']
# - Using ISO 8601 date formats for slicing
# ============================================

# 3. Python Script

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[
    (temperatures["date"] >= "2010-01-01") &
    (temperatures["date"] <= "2011-12-31")
]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010-01-01":"2011-12-31"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08-01":"2011-02-28"])

# ============================================
# 4. Additional Notes
# Slicing time series
# Slicing is especially useful for time series analysis. After setting
# the date column as the index and sorting it, you can subset ranges
# cleanly with .loc['start':'end'].
#
# Tips:
# - Keep dates in ISO 8601 format: "yyyy-mm-dd", "yyyy-mm", or "yyyy".
# - Combine multiple Boolean conditions with logical operators like &,
#   remembering to wrap each condition in parentheses.
#
# Context:
# pandas is loaded as pd, and `temperatures` is available with a 'date'
# column. (If needed, ensure 'date' is a datetime dtype via pd.to_datetime.)
# ============================================
