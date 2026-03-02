# ============================================
# 1. Task Description
# Compute quantiles of the CO₂ emission distribution from a food
# consumption dataset. Specifically, calculate deciles (10 groups) and a
# custom set of quantiles representing 0%, 20%, 40%, 60%, 80%, and 100%.
#
# 2. Topics Covered
# - Using numpy.quantile() for quantile calculations
# - Working with evenly spaced quantile cut points (np.linspace)
# - Summarizing numerical data via quartiles, quintiles, and deciles
# ============================================

# 3. Python Script

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption["co2_emission"], np.linspace(0, 1, 11)))

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption["co2_emission"], [0, 0.2, 0.4, 0.6, 0.8, 1]))

# ============================================
# 4. Additional Notes
# Quartiles, quantiles, and quintiles
# Quantiles divide a dataset into equal-sized segments and are widely used
# to summarize numerical distributions:
#
# - Quartiles → 4 groups  
# - Quintiles → 5 groups  
# - Deciles → 10 groups  
#
# In the example:
# - np.linspace(0, 1, 11) creates 11 evenly spaced values from 0 to 1,
#   giving the cut points for deciles.
# - A custom quantile list allows summarizing the distribution at any
#   chosen percentiles (e.g., 0%, 20%, 40%, 60%, 80%, 100%).
#
# Context:
# - pandas is imported as pd
# - numpy is imported as np
# - The DataFrame `food_consumption` is available and contains a column
#   named 'co2_emission'.
# ============================================
