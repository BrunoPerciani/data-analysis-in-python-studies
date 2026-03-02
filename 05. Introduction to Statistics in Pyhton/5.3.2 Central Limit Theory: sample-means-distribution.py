# ============================================
# 1. Task Description
# Demonstrate the Central Limit Theorem (CLT) by repeatedly sampling the
# num_users column from Amir's deals. Compute the mean of each sample and
# visualize the distribution of sample means to show how it approaches a
# normal distribution, regardless of the distribution of the original data.
#
# 2. Topics Covered
# - Random sampling with replacement
# - Computing sample means
# - Building a sampling distribution
# - Visualizing the CLT via histogram of sample means
# ============================================

# 3. Python Script

# Set seed to 104
np.random.seed(104)

sample_means = []

# Loop 100 times
for i in range(100):
    # Take sample of 20 num_users
    samp_20 = amir_deals["num_users"].sample(20, replace=True)
    # Calculate mean of samp_20
    samp_20_mean = np.mean(samp_20)
    # Append samp_20_mean to sample_means
    sample_means.append(samp_20_mean)

# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# The CLT in action
# - The Central Limit Theorem states that as sample size increases—or as
#   you take many repeated samples—the distribution of sample means becomes
#   approximately normal.
# - This holds *regardless* of the shape of the original distribution.
# - Here:
#     • We repeatedly sample 20 values from amir_deals["num_users"].
#     • We compute the mean for each sample.
#     • We visualize the distribution of these 100 sample means.
# - Even if num_users is skewed or irregular, the histogram of sample
#   means will appear more bell‑shaped.
#
# Context:
# pandas as pd, numpy as np, and matplotlib.pyplot as plt are loaded.
# The DataFrame `amir_deals` contains a column 'num_users'.
# ============================================
