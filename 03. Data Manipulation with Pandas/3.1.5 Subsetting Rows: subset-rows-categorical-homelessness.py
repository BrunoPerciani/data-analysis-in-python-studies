# ============================================
# 1. Task Description
# Subset rows of a DataFrame based on categorical variables using the
# .isin() method. The goal is to filter the homelessness dataset to
# include only rows for the Mojave Desert states.
#
# 2. Topics Covered
# - Subsetting rows by category
# - Using the .isin() method
# - Filtering multiple categories with a single condition
# ============================================

# 3. Python Script

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)

# ============================================
# 4. Additional Notes
# Subsetting rows by categorical variables
# When filtering by categories, using multiple OR conditions can become
# tedious. Instead, .isin() provides a cleaner and more scalable solution.
#
# Example:
#     colors = ["brown", "black", "tan"]
#     condition = dogs["color"].isin(colors)
#     dogs[condition]
#
# In this exercise:
# - We define a list of states belonging to the Mojave Desert.
# - We use .isin() to return only the rows where the "state" column
#   matches one of those entries.
#
# Note:
# The DataFrame `homelessness` is assumed to be available and pandas
# has already been imported as pd.
# ============================================
