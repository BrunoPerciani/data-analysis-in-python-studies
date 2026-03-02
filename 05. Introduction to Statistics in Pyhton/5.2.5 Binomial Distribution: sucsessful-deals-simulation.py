# ============================================
# 1. Task Description
# Simulate Amir’s weekly sales performance assuming he works on 3 deals
# per week and wins 30% of them. Model the number of weekly wins using a
# binomial distribution and compute the average number of deals won per
# week across 52 simulated weeks.
#
# 2. Topics Covered
# - Binomial distributions for binary outcomes
# - Random sampling with scipy.stats.binom.rvs()
# - Setting random seeds for reproducibility
# - Calculating sample means
# ============================================

# 3. Python Script

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3, 0.3, size=52)

# Print mean deals won per week
print(np.mean(deals))

# ============================================
# 4. Additional Notes
# Simulating sales deals
# - Each deal Amir works on is a binary outcome (win or loss).
# - The number of wins per week follows a Binomial(n=3, p=0.3) distribution:
#       n = 3 deals per week
#       p = 0.30 probability of winning each deal
# - Simulating 52 values mimics a full year of weekly performance.
# - Taking the mean gives the expected weekly success rate across the year.
#
# Context:
# numpy is imported as np, and scipy.stats.binom is used for simulations.
# ============================================
