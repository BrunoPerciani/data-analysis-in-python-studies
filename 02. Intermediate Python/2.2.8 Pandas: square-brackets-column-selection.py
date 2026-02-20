# ============================================
# 1. Task Description
# Demonstrate how to select columns from a pandas DataFrame using
# square brackets. Show the difference between:
#   • selecting a single column as a Series (single brackets)
#   • selecting a single column as a DataFrame (double brackets)
#   • selecting multiple columns at once
#
# This reinforces the fundamentals of pandas column indexing.
#
# 2. Topics Covered
# - DataFrame indexing with single vs. double brackets
# - Returning Series vs. DataFrame
# - Selecting multiple columns using lists
# ============================================

# 3. Python Script

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Print out 'country' column as a Pandas Series
print(cars['country'])

# Print out 'country' column as a Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with 'country' and 'drives_right'
print(cars[['country', 'drives_right']])

# ============================================
# 4. Additional Notes
# - A Series is 1-dimensional; a DataFrame is 2-dimensional.
# - Single brackets → Series:
#       type(cars['country'])
# - Double brackets → DataFrame:
#       type(cars[['country']])
# - Multiple-column selection always requires double brackets.
# ============================================
