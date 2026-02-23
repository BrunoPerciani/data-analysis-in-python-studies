# ============================================
# 1. Task Description
# Sort the homelessness DataFrame by region and then by family members
# in descending order within each region. The goal is to organize the
# data so that the highest family member counts appear first for each
# region.
#
# 2. Topics Covered
# - Sorting rows with .sort_values()
# - Sorting on multiple columns
# - Combining ascending and descending sort orders
# ============================================

# 3. Python Script

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(
    ["region", "family_members"], 
    ascending=[True, False]
)

print(homelessness_reg_fam.head())

# ============================================
# 4. Additional Notes
# Sorting rows
# Sorting rows helps reveal interesting patterns in a DataFrame. The method
# .sort_values() allows you to sort based on one or multiple columns.
#
# When sorting by a categorical variable (like region), multiple rows may
# share the same value. To break ties, you can sort by an additional
# column by passing a list of column names.
#
# In this example:
# - Rows are sorted alphabetically by region.
# - Within each region, rows are sorted by family_members in descending order.
#
# Note:
# The DataFrame `homelessness` is assumed to be available and already loaded.
# ============================================
