# ============================================
# 1. Task Description
# Determine which sequels earned more than their original movies by
# merging sequels with financials, then self-merging to compare the
# revenue of the original vs the sequel, computing the difference, and
# sorting the result.
#
# 2. Topics Covered
# - Left join to preserve all sequel rows
# - Self join to align original and sequel records
# - Vectorized arithmetic for revenue differences
# - Sorting results to find the largest gaps
# ============================================

# 3. Python Script

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on="id", how="left")

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(
    sequels_fin,
    how="inner",
    left_on="sequel",
    right_on="id",
    suffixes=("_org", "_seq")
)

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq["diff"] = orig_seq["revenue_seq"] - orig_seq["revenue_org"]

# Select the title_org, title_seq, and diff 
titles_diff = orig_seq[["title_org", "title_seq", "diff"]]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values("diff", ascending=False).head())

# ============================================
# 4. Additional Notes
# Do sequels earn more?
# - A left merge keeps all movies present in `sequels` even if their
#   financials are missing.
# - The self-merge aligns each original movie (left side) with its sequel
#   (right side) using the sequel's ID.
# - The 'diff' column shows how much more (or less) the sequel earned
#   compared to the original.
#
# Assumptions:
# - DataFrames `sequels` and `financials` are loaded.
# - Columns include:
#     sequels: id, title (→ title_org), sequel (id of sequel)
#     financials: id, revenue (→ revenue_org / revenue_seq after merge)
# ============================================
