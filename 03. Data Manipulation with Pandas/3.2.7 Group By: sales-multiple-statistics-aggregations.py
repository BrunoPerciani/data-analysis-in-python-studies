# ============================================
# 1. Task Description
# Compute multiple summary statistics on grouped data using the .agg()
# method. The goal is to calculate min, max, mean, and median weekly
# sales for each store type, as well as the same statistics for the
# unemployment and fuel_price_usd_per_l columns.
#
# 2. Topics Covered
# - Using .groupby() with .agg() for multiple summaries
# - Applying multiple statistics at once
# - Grouping data by a categorical variable
# - Summarizing multiple columns simultaneously
# ============================================

# 3. Python Script

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg(["min", "max", "mean", "median"])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l:
# get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg(
    ["min", "max", "mean", "median"]
)

# Print unemp_fuel_stats
print(unemp_fuel_stats)

# ============================================
# 4. Additional Notes
# Multiple grouped summaries
# The .agg() method allows you to compute several summary statistics at
# once, even on grouped data. This makes it easy to compare different
# metrics across categories.
#
# Examples:
# - Aggregating weekly_sales for each store type shows how performance
#   differs across store formats.
# - Aggregating unemployment and fuel_price_usd_per_l reveals how these
#   metrics behave within each store type.
#
# Context:
# The DataFrame `sales` is already available, and pandas is imported as pd.
# ============================================
