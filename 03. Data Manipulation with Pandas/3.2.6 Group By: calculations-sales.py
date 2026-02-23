# ============================================
# 1. Task Description
# Perform grouped calculations using the .groupby() method. The goal is to
# compute total weekly sales by store type, and then compute total weekly
# sales grouped by both store type and holiday status.
#
# 2. Topics Covered
# - Grouping data with .groupby()
# - Summing grouped values with .sum()
# - Grouping by multiple columns
# - Inspecting grouped results
# ============================================

# 3. Python Script

# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)

# ============================================
# 4. Additional Notes
# Calculations with .groupby()
# The .groupby() method is a powerful tool for calculating summary
# statistics across categories. It simplifies grouped arithmetic that
# would otherwise require multiple filtering steps.
#
# Examples:
# - sales.groupby("type")["weekly_sales"].sum()
#   returns total weekly sales by store type.
#
# - sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
#   reveals how total sales differ by store type depending on whether the
#   week was a holiday.
#
# Context:
# The DataFrame `sales` is available and pandas is already imported as pd.
# ============================================
