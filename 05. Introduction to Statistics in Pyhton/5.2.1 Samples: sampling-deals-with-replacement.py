# ============================================
# 1. Task Description
# Randomly sample five deals from Amir's sales records, using sampling
# *with replacement*. A random seed is set to ensure reproducibility.
#
# 2. Topics Covered
# - Setting a NumPy random seed
# - Random sampling with .sample()
# - Sampling with replacement (bootstrap-style sampling)
# ============================================

# 3. Python Script

# Set random seed
np.random.seed(24)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace=True)
print(sample_with_replacement)

# ============================================
# 4. Additional Notes
# Sampling deals
# Random sampling is useful for selecting a subset of observations for
# manual review or deeper inspection.
#
# - Setting the random seed ensures reproducibility so that the same
#   sample can be produced again.
# - replace=True enables sampling with replacement, meaning the same
#   deal can appear more than once in the sample.
#
# Context:
# - pandas is imported as pd
# - numpy is imported as np
# - The DataFrame `amir_deals` contains Amir's sales deals.
# ============================================
