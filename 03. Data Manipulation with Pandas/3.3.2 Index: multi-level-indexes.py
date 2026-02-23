# ============================================
# 1. Task Description
# Set a multi-level (hierarchical) index on a DataFrame and subset rows
# using label-based selection. The goal is to index temperatures by both
# country and city, then select specific country–city pairs with .loc.
#
# 2. Topics Covered
# - Creating a MultiIndex with .set_index()
# - Subsetting with .loc on multi-level indexes
# - Working with lists of tuple labels
# ============================================

# 3. Python Script

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# ============================================
# 4. Additional Notes
# Setting multi-level indexes
# Multi-level (hierarchical) indexes are useful for modeling nested
# categories (e.g., city nested within country). They can make reasoning
# about grouped data more natural, though index-based operations use a
# slightly different syntax than column-based operations.
#
# Tips:
# - Use .set_index(["col1", "col2"]) to create a MultiIndex.
# - Use .loc with tuples or lists of tuples to subset specific levels.
#
# Context:
# pandas is loaded as pd, and `temperatures` is available and contains
# average temperatures for cities around the world.
# ============================================
