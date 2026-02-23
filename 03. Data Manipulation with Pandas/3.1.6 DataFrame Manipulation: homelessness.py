# ============================================
# 1. Task Description
# Combine multiple DataFrame manipulations—adding new columns, subsetting
# rows, sorting, and subsetting columns—to answer an analytical question:
# "Which state has the highest number of homeless individuals per 10,000
# people in the state?"
#
# 2. Topics Covered
# - Creating new columns with vectorized arithmetic
# - Subsetting rows based on conditions
# - Sorting rows with .sort_values()
# - Selecting a subset of columns
# ============================================

# 3. Python Script

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)

# ============================================
# 4. Additional Notes
# Combo-attack!
# This exercise mixes the four common types of data manipulation:
# sorting rows, subsetting columns, subsetting rows, and adding new columns.
#
# Steps performed:
# 1) Create a per-capita metric (individuals per 10,000 people).
# 2) Filter for states above a chosen threshold (indiv_per_10k > 20).
# 3) Sort in descending order to find the highest values first.
# 4) Select only the relevant columns for the final answer.
#
# Assumptions:
# - The DataFrame `homelessness` is already loaded.
# - pandas is already imported as pd.
# ============================================
