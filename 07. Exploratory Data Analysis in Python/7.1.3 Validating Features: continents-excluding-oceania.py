# ============================================
# 1. Task Description
# Identify and remove unemployment records associated with Oceania.
# Use .isin() to create a Boolean mask that is True for all continents
# except Oceania, enabling filtering via Boolean indexing.
#
# 2. Topics Covered
# - Using .isin() to test membership in a list
# - Boolean negation (~) to invert selections
# - Filtering DataFrames with Boolean masks
# ============================================

# 3. Python Script

# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment["continent"].isin(["Oceania"])

# Print unemployment without records related to countries in Oceania
print(unemployment[not_oceania])

# ============================================
# 4. Additional Notes
# Validating continents
# - .isin(["Oceania"]) creates a Boolean Series where rows are True if
#   the continent is Oceania.
# - The tilde operator (~) negates the Series, turning:
#       Oceania  → False  
#       Others   → True
# - This Boolean mask is then used to filter out Oceania records.
#
# Use case:
# - When certain regional data is known to be unreliable or incomplete,
#   Boolean filtering enables fast exclusion prior to analysis.
#
# Context:
# pandas is imported as pd.
# The DataFrame `unemployment` includes a 'continent' column.
# ============================================
