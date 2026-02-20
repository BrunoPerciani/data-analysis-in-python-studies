# ============================================
# 1. Task Description
# Convert a dictionary of lists into a pandas DataFrame and then
# assign custom row labels. The default DataFrame index (0..6)
# should be replaced with meaningful labels (US, AUS, JPN, etc.)
# using the .index attribute.
#
# 2. Topics Covered
# - Creating a DataFrame from a Python dictionary
# - Assigning custom index labels using DataFrame.index
# - Basic pandas inspection with print()
# ============================================

import pandas as pd

# 3. Python Script

# Build cars DataFrame from dictionary of lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

cars = pd.DataFrame(cars_dict)
print(cars)  # print DataFrame with default integer index

# Definition of custom row labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Assign custom index to the DataFrame
cars.index = row_labels

# Print DataFrame with updated row labels
print(cars)

# ============================================
# 4. Additional Notes
# - Setting cars.index replaces the existing index in place.
# - To avoid mutating the original, you could also do:
#       cars = pd.DataFrame(cars_dict, index=row_labels)
# - Row labels can be any hashable Python object (strings, ints, tuples).
# ============================================
