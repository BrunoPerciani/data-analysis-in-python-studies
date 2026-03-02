# ============================================
# 1. Task Description
# Perform a semi join to identify which non-musical tracks appear in the
# list of top revenue-generating invoices. Then count these tracks by
# genre and merge with the genres table to label the results.
#
# 2. Topics Covered
# - Semi join pattern using .isin()
# - Merging DataFrames to align related tables
# - Grouping and counting with .groupby().agg()
# - Labeling grouped output via merging with a lookup table
# ============================================

# 3. Python Script

# Merge the non_mus_tcks and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on="tid")

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks["tid"].isin(tracks_invoices["tid"])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(["gid"], as_index=False).agg({"tid": "count"})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on="gid"))

# ============================================
# 4. Additional Notes
# Performing a semi join
# A semi join keeps only rows from the left table that have at least one
# match in the right table, without duplicating rows from the right.
#
# Steps performed:
# - Merge non_mus_tcks ⨝ top_invoices on tid to find matches.
# - Use .isin() to keep only non-musical tracks that appear in invoices.
# - Group by gid to count how many top tracks belong to each genre.
# - Merge with genres to label each gid with its genre name.
#
# Context:
# The DataFrames `non_mus_tcks`, `top_invoices`, and `genres` are loaded.
# pandas is imported as pd.
# ============================================
