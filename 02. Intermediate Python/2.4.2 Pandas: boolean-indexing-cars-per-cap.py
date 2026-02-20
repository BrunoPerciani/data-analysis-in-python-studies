# ============================================
# 1. Task Description
# Filter the cars DataFrame to select countries whose cars_per_cap
# value lies between 100 and 500 (exclusive). This requires building
# a boolean mask using NumPy’s logical operators, which work element‑wise
# on pandas Series.
#
# 2. Topics Covered
# - Boolean masking with pandas Series
# - np.logical_and() to combine conditions
# - Advanced DataFrame filtering using boolean arrays
# ============================================

# 3. Python Script

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Import numpy for logical operations
import numpy as np

# Select cars_per_cap column
cpc = cars['cars_per_cap']

# Create boolean mask: True where 100 < cars_per_cap < 500
between = np.logical_and(cpc > 100, cpc < 500)

# Apply mask to filter the DataFrame
medium = cars[between]

# Print result
print(medium)

# ============================================
# 4. Additional Notes
# - Equivalent boolean expression using pandas syntax:
#       medium = cars[(cpc > 100) & (cpc < 500)]
# - np.logical_or() and np.logical_not() work similarly:
#       np.logical_or(cond1, cond2)
#       np.logical_not(cond)
# - Boolean masks must align with the DataFrame index.
# ============================================
