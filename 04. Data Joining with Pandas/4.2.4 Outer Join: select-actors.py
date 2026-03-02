# ============================================
# 1. Task Description
# Use an outer join to identify actors who appeared in only one of the
# two movies: Iron Man 1 or Iron Man 2. Outer joins return all rows from
# both tables, and missing matches appear as null values, allowing us to
# detect actors not present in both movies.
#
# 2. Topics Covered
# - Outer joins with .merge(how="outer")
# - Using suffixes to keep track of overlapping column names
# - Detecting non-matching rows via null checks
# - Filtering and previewing results
# ============================================

# 3. Python Script

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(
    iron_2_actors,
    on="id",
    how="outer",
    suffixes=("_1", "_2")
)

# Create an index that returns true if name_1 or name_2 are null
m = (iron_1_and_2["name_1"].isnull()) | (iron_1_and_2["name_2"].isnull())

# Print the first few rows of iron_1_and_2 for actors missing from one table
print(iron_1_and_2[m].head())

# ============================================
# 4. Additional Notes
# Using outer join to select actors
# A key advantage of outer joins is that they preserve all rows from both
# tables, inserting nulls where there are no matches. This makes it easy
# to identify:
# - Actors who appeared in Iron Man 1 but not Iron Man 2.
# - Actors who appeared in Iron Man 2 but not Iron Man 1.
#
# Steps:
# 1) Perform an outer join on actor IDs.
# 2) Look for rows where either name_1 or name_2 is null.
# 3) These rows represent actors who participated in only one of the movies.
#
# Context:
# The DataFrames `iron_1_actors` and `iron_2_actors` are preloaded.
# pandas is imported as pd.
# ============================================
