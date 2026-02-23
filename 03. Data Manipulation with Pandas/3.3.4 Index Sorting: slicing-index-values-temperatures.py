# ============================================
# 1. Task Description
# Practice slicing a DataFrame by index values using .loc[] with a
# sorted index. The goal is to slice ranges at the outer and inner
# levels of a MultiIndex.
#
# 2. Topics Covered
# - Sorting an index with .sort_index()
# - Slicing by outer-level labels (strings)
# - Slicing by inner-level labels (tuples) in a MultiIndex
# - Using .loc[first:last] slice syntax
# ============================================

# 3. Python Script

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Philippines
print(temperatures_srt.loc["Pakistan":"Philippines"])

# Try to subset rows from Lahore to Manila
print(temperatures_srt.loc["Lahore":"Manila"])

# Subset rows from Pakistan, Lahore to Philippines, Manila
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Philippines", "Manila")])

# ============================================
# 4. Additional Notes
# Slicing index values
# Slicing selects consecutive elements using first:last syntax.
# With DataFrames, slicing can be done by index labels using .loc[].
#
# Key points:
# - You can only slice by index labels if the index is sorted.
# - For slices at the outer level of a MultiIndex, use strings:
#       df.loc["Pakistan":"Philippines"]
# - For slices that include inner levels, use tuples:
#       df.loc[("Pakistan", "Lahore"):("Philippines", "Manila")]
# - Passing a single slice to .loc[] slices the rows.
#
# Context:
# pandas is loaded as pd. `temperatures_ind` is a MultiIndex DataFrame
# with ("country", "city") as index levels.
# ============================================
