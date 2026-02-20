# ============================================
# 1. Task Description
# Identify which countries in the cars DataFrame have a high number
# of cars per capita. To do this, build a boolean Series based on
# a threshold (cars_per_cap > 500), and use it to filter the DataFrame.
# This is a typical example of boolean indexing in pandas.
#
# 2. Topics Covered
# - Boolean Series creation
# - Filtering DataFrames with boolean conditions
# - Column selection via single brackets
# ============================================

# 3. Python Script

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Create boolean Series: True where cars_per_cap > 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500

# Subset the DataFrame using the boolean mask
car_maniac = cars[many_cars]

# Print result
print(car_maniac)

# ============================================
# 4. Additional Notes
# - Boolean indexing is one of pandas’ most powerful tools:
#       filtered_df = df[df['column'] > value]
# - Boolean Series must have the same index as the DataFrame.
# - You can combine conditions using &, |, and ~:
#       df[(df['col1'] > 10) & (df['col2'] < 5)]
# ============================================
