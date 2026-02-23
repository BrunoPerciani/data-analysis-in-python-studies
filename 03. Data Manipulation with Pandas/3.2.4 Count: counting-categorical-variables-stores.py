# ============================================
# 1. Task Description
# Count the occurrences and proportions of categorical values within the
# sales dataset. The goal is to compute counts and proportions for store
# types and departments using DataFrames created in a previous step.
#
# 2. Topics Covered
# - Counting categories with .value_counts()
# - Getting proportions with normalize=True
# - Sorting results
# - Working with deduplicated DataFrames
# ============================================

# 3. Python Script

# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of stores for each department and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of stores in each department and sort
dept_props_sorted = store_depts["department"].value_counts(
    sort=True, normalize=True
)
print(dept_props_sorted)

# ============================================
# 4. Additional Notes
# Counting categorical variables
# Counting categories is a powerful way to quickly understand the
# distribution of categorical values in a dataset. It helps reveal
# patterns and potential anomalies.
#
# Examples:
# - store_types["type"].value_counts() returns how many stores belong
#   to each store type.
# - store_depts["department"].value_counts() shows how many stores
#   contain each department.
#
# Using normalize=True converts counts into proportions, making it easy
# to understand relative frequencies.
#
# Context:
# The following DataFrames are assumed to exist:
#     store_types = sales.drop_duplicates(subset=["store", "type"])
#     store_depts  = sales.drop_duplicates(subset=["store", "department"])
#
# pandas has already been imported as pd.
# ============================================
