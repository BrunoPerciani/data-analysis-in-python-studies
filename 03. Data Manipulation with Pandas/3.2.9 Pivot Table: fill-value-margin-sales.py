# ============================================
# 1. Task Description
# Create a pivot table showing the sum of weekly sales grouped by
# department (rows) and store type (columns). The goal is to fill missing
# values with zeros and include row/column totals.
#
# 2. Topics Covered
# - Using .pivot_table() for grouped aggregation
# - Handling missing values with fill_value
# - Adding row and column totals with margins=True
# - Summing values across multiple categories
# ============================================

# 3. Python Script

# Print the mean weekly_sales by department and type;
# fill missing values with 0s; sum all rows and cols
print(
    sales.pivot_table(
        values="weekly_sales",
        index="department",
        columns="type",
        aggfunc="sum",
        fill_value=0,
        margins=True
    )
)

# ============================================
# 4. Additional Notes
# Fill in missing values and sum values with pivot tables
# The pivot_table() method supports several helpful arguments:
#
# - fill_value:
#     Replaces missing values in the resulting table.  
#     This is known as imputation. A simple and common approach is to
#     replace missing entries with 0, especially when aggregating sums.
#
# - margins:
#     Adds row and column totals to the pivot table.  
#     This is equivalent to performing additional grouped aggregations
#     by each variable separately.
#
# Example:
#     df.pivot_table(values="x", index="A", columns="B",
#                    aggfunc="sum", fill_value=0, margins=True)
#
# Context:
# The DataFrame `sales` is available and pandas has been imported as pd.
# ============================================
