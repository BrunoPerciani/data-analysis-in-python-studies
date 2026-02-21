# ============================================
# 1. Task Description
# Add a new column called 'COUNTRY' to the cars DataFrame by looping
# through each row with .iterrows() and storing the uppercase version
# of the existing 'country' field. This exercise reinforces row-wise
# assignment using .loc to update a DataFrame.
#
# 2. Topics Covered
# - DataFrame iteration with .iterrows()
# - Updating DataFrame cells using .loc
# - String transformation with .upper()
# ============================================

# 3. Python Script

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Loop over the rows and add a new uppercase COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print updated DataFrame
print(cars)

# ============================================
# 4. Additional Notes
# - Using .loc[lab, "COUNTRY"] ensures assignment respects the index.
# - For performance on large DataFrames, prefer vectorized operations:
#       cars["COUNTRY"] = cars["country"].str.upper()
# - .iterrows() returns (index, Series); Series behaves like a dict.
# ============================================
