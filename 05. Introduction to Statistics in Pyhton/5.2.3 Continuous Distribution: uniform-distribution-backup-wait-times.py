# ============================================
# 1. Task Description
# Model Amir's expected wait time for an automatic data back-up that
# occurs exactly every 30 minutes using the continuous uniform
# distribution. Compute the probability that he will have to wait between
# 10 and 20 minutes after entering new data.
#
# 2. Topics Covered
# - Continuous uniform distributions
# - Using scipy.stats.uniform
# - Calculating probabilities with cumulative distribution functions (CDF)
# - Computing P(a < X < b) via CDF differences
# ============================================

# 3. Python Script

# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20, min_time, max_time) - uniform.cdf(10, min_time, max_time)
print(prob_between_10_and_20)

# ============================================
# 4. Additional Notes
# Data back-ups
# - If backups occur exactly every 30 minutes and Amir arrives at a random
#   time, the wait time is uniformly distributed between 0 and 30 minutes.
#
# - For a continuous uniform distribution on [a, b], the CDF is:
#       F(x) = (x - a) / (b - a)
#   and the probability of waiting between times t1 and t2 is:
#       P(t1 < X < t2) = F(t2) - F(t1)
#
# - Here:
#       a = 0
#       b = 30
#       P(10 < X < 20) = F(20) – F(10)
#
# Context:
# pandas is imported as pd, numpy as np, and scipy.stats.uniform is used
# for probability calculations. The DataFrame `amir_deals` is not needed
# for this exercise.
# ============================================
