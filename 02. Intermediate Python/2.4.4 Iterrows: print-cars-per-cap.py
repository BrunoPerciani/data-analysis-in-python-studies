# ============================================
# 1. Task Description
# Loop over all rows in the cars DataFrame using .iterrows().
# For each row, print the label (index) together with the value
# in the 'cars_per_cap' column. This exercise reinforces how to
# iterate through DataFrame rows and access individual column
# values from the resulting Series.
#
# 2. Topics Covered
# - DataFrame row iteration with .iterrows()
# - Accessing Series values inside the loop
# - Combining labels (index) and row data
# ============================================

# 3. Python Script

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Loop through the DataFrame, printing index + cars_per_cap value
for lab, row in cars.iterrows():
    print(lab + ": " + str(row['cars_per_cap']))

# ============================================
# 4. Additional Notes
# - iterrows() returns (index, Series) pairs.
# - Access values using row['column_name'].
# - iterrows() is slow for large DataFrames; vectorized operations are preferred.
# - Alternative using .itertuples() (faster):
#       for row in cars.itertuples():
#           print(row.Index, row.cars_per_cap)
# ============================================
