# ============================================
# 1. Task Description
# Simulate Amir's wait time for a system backup that occurs uniformly
# between 0 and 30 minutes, generating 1000 random wait times and
# visualizing the distribution with a histogram.
#
# 2. Topics Covered
# - Random sampling from a continuous uniform distribution
# - Using scipy.stats.uniform.rvs()
# - Setting random seeds for reproducibility
# - Plotting histograms with matplotlib
# ============================================

# 3. Python Script

# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()

# ============================================
# 4. Additional Notes
# Simulating wait times
# - Amir’s wait time follows a continuous uniform distribution on [0, 30],
#   because backups occur exactly every 30 minutes and his arrival is random.
# - uniform.rvs(a, b, size) generates random samples where 'a' is the
#   minimum value and 'b' is the range.
# - Setting a seed ensures reproducibility so the same 1000 samples can be
#   generated again.
# - The histogram visualizes the simulated wait-time distribution, which
#   should be roughly flat, characteristic of a uniform distribution.
#
# Context:
# pandas is imported as pd, numpy as np, and matplotlib.pyplot as plt.
# ============================================
