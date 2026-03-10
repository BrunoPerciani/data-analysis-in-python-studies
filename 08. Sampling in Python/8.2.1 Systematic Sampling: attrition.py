# ============================================
# 1. Task Description
# Perform systematic sampling on the attrition population dataset.
# Select 70 evenly spaced observations by computing the sampling interval
# and selecting every k-th row from the population.
#
# 2. Topics Covered
# - Systematic sampling with pandas
# - Computing sampling intervals
# - Understanding sample size vs. population size
# ============================================

# 3. Python Script

# Set the sample size to 70
sample_size = 70

# Calculate the population size from attrition_pop
pop_size = len(attrition_pop)

# Calculate the interval
interval = pop_size // sample_size

# Systematically sample 70 rows
attrition_sys_samp = attrition_pop.iloc[::interval]

# Print the sample
print(attrition_sys_samp)

# ============================================
# 4. Additional Notes
# Systematic sampling
# - Unlike random sampling, systematic sampling selects observations at
#   a fixed interval determined by:
#         interval = population_size // sample_size
# - The sample is created by taking rows:
#         0, interval, 2*interval, 3*interval, ...
# - This method is simple, deterministic, and ensures good coverage of
#   the entire dataset—especially when the data has no hidden ordering bias.
#
# Caution:
# - If
