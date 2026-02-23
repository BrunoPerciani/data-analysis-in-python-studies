# ============================================
# 1. Task Description
# Compute cumulative statistics on a sales time series to track how
# totals and peaks evolve over time. The goal is to calculate the
# cumulative sum and cumulative maximum of weekly sales.
#
# 2. Topics Covered
# - Sorting time series data
# - Cumulative sum with .cumsum()
# - Cumulative maximum with .cummax()
# - Selecting and printing relevant columns
# ============================================

# 3. Python Script

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date")

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

# ============================================
# 4. Additional Notes
# Cumulative statistics
# Cumulative statistics are useful to track running totals and records
# over time. In this exercise, we:
# - Sort by date to ensure chronological order.
# - Compute a running total using .cumsum().
# - Compute the running peak using .cummax().
#
# Context:
# A DataFrame called `sales_1_1` contains weekly sales for department 1
# of store 1.
#
# Note:
# pandas is already imported as pd, and `sales_1_1` is assumed to be loaded.
# ============================================
