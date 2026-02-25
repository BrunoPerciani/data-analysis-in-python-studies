# ============================================
# 1. Task Description
# Merge land use, census, and business license data to analyze which
# Chicago wards have high vacant land, low population, and fewer
# businesses. This helps determine ideal locations for a hypothetical
# goat-farming business needing open space and minimal neighborhood
# conflict.
#
# 2. Topics Covered
# - One-to-many merges across multiple tables
# - Using suffixes to distinguish overlapping columns
# - Grouping by multiple variables
# - Counting matches with .agg({"account": "count"})
# - Sorting by several fields for prioritization
# ============================================

# 3. Python Script

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = (
    land_use.merge(census, on="ward")
            .merge(licenses, on="ward", suffixes=("_cen", "_lic"))
)

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(
    ["ward", "pop_2010", "vacant"], as_index=False
).agg({"account": "count"})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(
    ["vacant", "account", "pop_2010"],
    ascending=[False, True, True]
)

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())

# ============================================
# 4. Additional Notes
# One-to-many merge with multiple tables
# This exercise demonstrates merging three related tables:
#
# - land_use: percentage of vacant land per ward
# - census: population by ward
# - licenses: businesses by ward
#
# Steps:
# 1) Merge land_use ⨝ census on 'ward'
# 2) Merge the result ⨝ licenses on 'ward', using suffixes to avoid
#    column name collisions
# 3) Group by ward, population, and vacant land percentage
# 4) Count businesses (accounts) per group
# 5) Sort by highest vacancy, fewest businesses, and lowest population
#
# Interpretation:
# Wards with high vacant land, few businesses, and low population are
# ideal candidates for locating a goat-farming business.
#
# Context:
# The DataFrames `land_use`, `census`, and `licenses` have been loaded.
# pandas is imported as pd.
# ============================================
