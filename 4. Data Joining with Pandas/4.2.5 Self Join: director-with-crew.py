# ============================================
# 1. Task Description
# Perform a self join on the crews table to pair each movie's director
# with other crew members on the same movie. The goal is to merge the
# table to itself on movie ID, then filter rows so that the left-side job
# is 'Director' and the right-side job is not 'Director'.
#
# 2. Topics Covered
# - Self join (merging a table to itself)
# - Using suffixes to distinguish duplicate column names
# - Boolean filtering on merged results
# - Previewing the output with .head()
# ============================================

# 3. Python Script

# Merge the crews table to itself
crews_self_merged = crews.merge(
    crews,
    on="id",
    how="inner",
    suffixes=("_dir", "_crew")
)

# Create a boolean index to select the appropriate rows
boolean_filter = (
    (crews_self_merged["job_dir"] == "Director") &
    (crews_self_merged["job_crew"] != "Director")
)
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())

# ============================================
# 4. Additional Notes
# Self join
# Self joins are useful for comparing rows within the same table. Here, we
# pair the director (left side) with each other crew role (right side) for
# the same movie, using the shared movie ID as the join key.
#
# Steps:
# - Merge crews with itself on 'id' (movie ID), adding suffixes to tell
#   director-side columns (_dir) from crew-side columns (_crew).
# - Filter to keep only rows where the left job is 'Director' and the
#   right job is not 'Director'.
# - The result lists, for each movie, the director alongside each
#   non-director crew member.
#
# Context:
# The DataFrame `crews` contains columns: id, job, and name.
# pandas has been imported as pd.
# ============================================
