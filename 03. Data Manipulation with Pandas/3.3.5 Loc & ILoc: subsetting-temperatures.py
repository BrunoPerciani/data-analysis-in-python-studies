# ============================================
# 1. Task Description
# Subset a DataFrame by row and column number using .iloc[]. The goal is
# to select specific elements, slice by row ranges, slice by column
# ranges, and slice both dimensions simultaneously.
#
# 2. Topics Covered
# - Indexing by row/column number with .iloc[]
# - Selecting a single element
# - Slicing rows
# - Slicing columns
# - Slicing rows and columns at the same time
# ============================================

# 3. Python Script

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[24, 1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[0:6, :])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[0:6, 2:4])

# ============================================
# 4. Additional Notes
# Subsetting by row/column number
# While subsetting by Boolean conditions or index labels is common,
# .iloc[] allows you to subset by can pass slices for rows, columns, or both.
# - Slicing syntax is the same as standard Python: start:stop (stop excluded).
#
# Examples:
#     df.iloc[10, 3]       → element at row 10, column 3
#     df.iloc[0:5, :]      → first 5 rows
#     df.iloc[:, 1:3]      → columns 1 and 2
#     df.iloc[0:5, 1:3]    → first 5 rows, columns 1–2
#
# Context:
# pandas is loaded as pd, and `temperatures` is available with default
# integer index and full column set.
# ============================================
