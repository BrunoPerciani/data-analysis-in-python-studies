# ============================================
# 1. Task Description
# Create a custom function to compute the interquartile range (IQR) and use
# the .agg() method to efficiently summarize multiple columns in a DataFrame.
# The goal is to print the IQR and the median for temperature_c,
# fuel_price_usd_per_l, and unemployment.
#
# 2. Topics Covered
# - Writing a custom summary function
# - Using .agg() to apply multiple aggregations across multiple columns
# - Computing IQR (Q3 - Q1) and median
# ============================================

# 3. Python Script

# Create a custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, "median"]))

# ============================================
# 4. Additional Notes
# Efficient summaries
# While pandas and NumPy provide a wide range of functions, sometimes you
# need a custom summary for your data. The .agg() method allows you to:
# - Apply your own functions to Series or DataFrames.
# - Apply more than one function at once.
#
# Example:
#     df["column"].agg(function)
#
# In this exercise, "IQR" stands for interquartile range and is computed as
# the 75th percentile minus the 25th percentile (Q3 - Q1). It is a robust
# alternative to standard deviation when your data may contain outliers.
#
# Assumptions:
# - The DataFrame `sales` is available.
# - pandas has already been imported as pd.
# ============================================
