# ============================================
# 1. Task Description
# Use .loc and .iloc to select specific rows and columns from a
# pandas DataFrame. Demonstrate:
#   • selecting a single value using row+column labels (loc)
#   • selecting multiple rows and columns as a sub‑DataFrame (loc)
#   • reinforcing that loc (label‑based) and iloc (integer‑based)
#     indexing can retrieve the same elements.
#
# 2. Topics Covered
# - pandas DataFrame label‑based indexing (loc)
# - pandas DataFrame integer‑based indexing (iloc)
# - Selecting scalars, rows, columns, and sub‑DataFrames
# ============================================

# 3. Python Script

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Print out drives_right value of Morocco (label-based selection)
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame for Russia and Morocco with specific columns
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# ============================================
# 4. Additional Notes
# - loc uses **labels**:
#       cars.loc['IN', 'cars_per_cap']
# - iloc uses **integer positions**:
#       cars.iloc[3, 0]
#
# Examples (equivalent pairs):
#   • Scalar:
#       cars.loc['IN', 'cars_per_cap']    == cars.iloc[3, 0]
#
#   • Selecting two rows, one column:
#       cars.loc[['IN', 'RU'], 'cars_per_cap']
#       cars.iloc[[3, 4], 0]
#
#   • Selecting rows and multiple columns:
#       cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
#       cars.iloc[[3, 4], [0, 1]]
#
# loc is generally more readable when meaningful row labels exist.
# ============================================
