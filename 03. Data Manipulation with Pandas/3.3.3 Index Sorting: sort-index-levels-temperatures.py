# ============================================
# 1. Task Description
# Sort a DataFrame using its index values. The goal is to practice
# sorting by a multi-level index (country, city), sorting by specific
# index levels, and sorting with ascending/descending combinations.
#
# 2. Topics Covered
# - Sorting a DataFrame with .sort_index()
# - Sorting by specific index levels
# - Sorting multi-level indexes in mixed ascending orders
# ============================================

# 3. Python Script

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))

# Sort temperatures_ind by country then descending city
print(
    temperatures_ind.sort_index(
        level=["country", "city"],
        ascending=[True, False]
    )
)

# ============================================
# 4. Additional Notes
# Sorting by index values
# While .sort_values() sorts rows based on column values,
# .sort_index() sorts rows based on index labels.
#
# With multi-level indexes:
# - level="city" sorts only by the city level of the index.
# - level=["country", "city"] sorts first by country, then by city.
# - ascending accepts a list for per-level sort order.
#
# Context:
# pandas is loaded as pd.
# `temperatures_ind` is available and has a MultiIndex
# with levels ["country", "city"].
# ============================================
