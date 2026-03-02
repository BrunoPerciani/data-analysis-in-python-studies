# ============================================
# 1. Task Description
# Concatenate yearly classical and pop playlist tables to build combined
# datasets for 2018–2019. Then, merge them to identify common tracks and
# semi-join the classical playlist to return only those classical tracks
# that also appear in the popular (pop) playlist.
#
# 2. Topics Covered
# - Vertical concatenation with pd.concat()
# - Merging tables to find overlaps
# - Semi join pattern using .isin()
# - Subsetting and previewing results
# ============================================

# 3. Python Script

# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on="tid")

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19["tid"].isin(classic_pop["tid"])]

# Print popular chart
print(popular_classic)

# ============================================
# 4. Additional Notes
# Concatenate and merge to find common songs
# - Concatenation combines yearly files into larger tables for analysis.
# - Merging on 'tid' reveals tracks that exist in both classical and pop
#   playlists (i.e., common tracks).
# - The semi join is implemented with .isin(), retaining only classical
#   tracks whose 'tid' also appears in the merged overlap.
#
# Context:
# The DataFrames `classic_18`, `classic_19`, `pop_18`, and `pop_19` are
# preloaded. pandas has been imported as pd.
# ============================================
