# ============================================
# 1. Task Description
# Demonstrate how to select columns from a pandas DataFrame using
# square brackets. Show the difference between selecting a single
# column as a Series (using single brackets) and selecting one or
# multiple columns as a DataFrame (using double brackets).
#
# 2. Topics Covered
# - pandas DataFrame indexing with square brackets
# - Selecting a single column as a Series vs. as a DataFrame
# - Selecting multiple columns at once
# ============================================

# 3. Python Script

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Print out country column as Pandas Series (1D)
print(cars['country'])

# Print out country column as Pandas DataFrame (2D)
print(cars[['country']])

# Print out DataFrame with both 'country' and 'drives_right' columns
print(cars[['country', 'drives_right']])

# ============================================
# 4. Additional Notes
# - Using single brackets returns a Series:
#       type(cars['country']) → pandas.Series
# - Using double brackets returns a DataFrame:
#       type(cars[['country']]) → pandas.DataFrame
# - When selecting multiple columns, always use double brackets.
# ============================================
