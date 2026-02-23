# ============================================
# 1. Task Description
# Create a pivot table to calculate the mean and median weekly sales
# grouped by store type and holiday status. The goal is to replicate
# grouped calculations using the pivot_table() method.
#
# 2. Topics Covered
# - Creating pivot tables with .pivot_table()
# - Aggregating with multiple functions (mean and median)
# - Grouping data by index and columns simultaneously
# - Replicating groupby-style summaries with pivot tables
# ============================================

# 3. Python Script

# Pivot for mean and median weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(
    values="weekly_sales",
    index="type",
    columns="is_holiday",
    aggfunc=["mean", "median"]
)

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

# ============================================
# 4. Additional Notes
# Pivoting on one variable
# Pivot tables are a standard way of aggregating data in spreadsheets.
# In pandas, pivot_table() is an alternative to groupby() for producing
# grouped summary statistics.
#
# Example:
# sales.pivot_table(values="weekly_sales", index="type",
#                   columns="is_holiday", aggfunc="mean")
#
# In this exercise:
# - The index ("type") defines row groups.
# - The columns ("is_holiday") define subgroups.
# - The aggfunc list computes both mean and median simultaneously.
#
# Context:
# The DataFrame `sales` is available and pandas has been imported as pd.
# ============================================
