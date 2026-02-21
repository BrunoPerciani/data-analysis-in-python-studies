# ============================================
# 1. Task Description
# Add a new column called 'COUNTRY' to the cars DataFrame by applying
# the .upper() string method to each element of the existing 'country'
# column. This exercise demonstrates the use of .apply() for efficient,
# vectorized DataFrame column transformations.
#
# 2. Topics Covered
# - Vectorized operations with pandas
# - Column-wise transformations using .apply()
# - String methods applied to Series
# ============================================

# 3. Python Script

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Use .apply(str.upper) to create an uppercase COUNTRY column
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print updated DataFrame
print(cars)

# ============================================
# 4. Additional Notes
# - .apply() is far more efficient than looping with .iterrows().
# - For string operations, pandas also offers .str.upper():
#       cars["COUNTRY"] = cars["country"].str.upper()
# - .apply() works with any Python function, including custom ones:
#       cars["col"] = cars["col"].apply(lambda x: custom_function(x))
# ============================================
