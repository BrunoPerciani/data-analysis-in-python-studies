# ============================================
# 1. Task Description
# Estimate the company's average number of users per deal by repeatedly
# sampling from all_deals, then compare this estimate to Amir’s own
# average number of users per deal. This demonstrates how sample means
# approximate population means.
#
# 2. Topics Covered
# - Random sampling with replacement
# - Computing sample means
# - Repeated sampling to estimate a population statistic
# - Comparing sample‑based estimates to a subgroup mean
# ============================================

# 3. Python Script

# Set seed to 321
np.random.seed(321)

sample_means = []

# Loop 30 times to take 30 means
for i in range(30):
    # Take sample of size 20 from num_users col of all_deals with replacement
    cur_sample = all_deals["num_users"].sample(20, replace=True)
    # Take mean of cur_sample
    cur_mean = np.mean(cur_sample)
    # Append cur_mean to sample_means
    sample_means.append(cur_mean)

# Print mean of sample_means
print(np.mean(sample_means))

# Print mean of num_users in amir_deals
print(np.mean(amir_deals["num_users"]))

# ============================================
# 4. Additional Notes
# The mean of means
# - When the full population (all deals) is too large to compute directly,
#   repeated random samples can be used to estimate the population mean.
# - The average of the sample means is itself an unbiased estimator of the
#   true population mean.
# - Comparing:
#       (1) mean(sample_means)
#       (2) mean(amir_deals["num_users"])
#   helps determine whether Amir typically works with more or fewer users
#   than the company overall.
#
# Context:
# pandas as pd and numpy as np are loaded.
# `amir_deals` and `all_deals` DataFrames are available.
# ============================================
