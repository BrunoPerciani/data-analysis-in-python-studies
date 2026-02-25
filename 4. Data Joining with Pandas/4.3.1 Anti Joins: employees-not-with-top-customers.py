# ============================================
# 1. Task Description
# Perform an anti join to identify employees who are not assigned to any
# top customers. The goal is to left-merge employees with top_cust and
# filter rows that only appear on the left side (employees).
#
# 2. Topics Covered
# - Left join with merge(how="left", indicator=True)
# - Anti join pattern using _merge == "left_only"
# - Boolean indexing with .loc and .isin()
# - Subsetting a DataFrame by IDs
# ============================================

# 3. Python Script

# Merge employees and top_cust
empl_cust = employees.merge(
    top_cust,
    on="srid",
    how="left",
    indicator=True
)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust["_merge"] == "left_only", "srid"]

# Get employees not working with top customers
print(employees[employees["srid"].isin(srid_list)])

# ============================================
# 4. Additional Notes
# Performing an anti join
# An anti join returns rows from the left table that have no match in the
# right table. In pandas, simulate it by:
# 1) Doing a left merge with indicator=True to track match status.
# 2) Filtering rows where _merge == "left_only".
#
# In this exercise:
# - employees: employee representatives (key: srid)
# - top_cust: table of top customers with their assigned srid
# - Result: list of employees who are not assigned to any top customers,
#   so leadership can allocate training or reassignments.
#
# Context:
# The DataFrames `top_cust` and `employees` are preloaded.
# pandas is imported as pd.
# ============================================
