# ============================================
# 1. Task Description
# Explore how inner joins affect the number of rows returned when key
# values don't match across tables. We'll compare a standard merge between
# wards and census with a merge that uses an altered version of census
# (census_altered) in which the first row's ward value has been changed.
#
# 2. Topics Covered
# - Inner joins with .merge()
# - Matching keys and row retention
# - Inspecting shapes before/after merging
# - Understanding how altered keys reduce matches
# ============================================

# 3. Python Script

# Print the first few rows of the census_altered table to view the change 
print(census_altered[["ward"]].head())

# Merge the wards and census_altered tables on the ward column
wards_census_altered = wards.merge(census_altered, on="ward")

# Print the shape of wards_census_altered
print("wards_census_altered table shape:", wards_census_altered.shape)

# ============================================
# 4. Additional Notes
# Inner joins and number of rows returned
# Inner joins only return rows where the join keys exist in both tables.
# If a key is altered in one table (e.g., the first 'ward' in
# census_altered), those records no longer match and are dropped from the
# result.
#
# Context:
# - The original wards and census tables each start with 50 rows.
# - Altering a key value (such as the first 'ward') reduces the number
#   of matches, which will typically decrease the number of rows in the
#   merged output compared to merging the unaltered tables.
#
# Tip:
# - Use .shape to quickly verify the impact of merges on row counts.
# - Inspecting the key column (e.g., 'ward') with .head() helps confirm
#   where mismatches may occur.
# ============================================
