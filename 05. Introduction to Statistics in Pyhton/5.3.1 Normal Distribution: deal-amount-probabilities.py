# ============================================
# 1. Task Description
# Using the normal distribution of Amir’s deal amounts (mean = 5000,
# standard deviation = 2000), compute several probability-based metrics:
# - The 25th percentile (value that 25% of deals fall below)
# - The probability a deal is between 3000 and 7000
# - The probability a deal is greater than 1000
# - The probability a deal is less than 7500
#
# 2. Topics Covered
# - Using norm.ppf() to compute quantiles
# - Using norm.cdf() to compute probabilities
# - Interpreting values under a normal distribution
# ============================================

# 3. Python Script

# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25, 5000, 2000)
print(pct_25)

# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)
print(prob_3000_to_7000)

# Probability of deal > 1000
prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)
print(prob_over_1000)

# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, 5000, 2000)
print(prob_less_7500)

# ============================================
# 4. Additional Notes
# Probabilities from the normal distribution
# - norm.ppf(q, mean, sd) returns the value x such that P(X ≤ x) = q.
#   Here, the 25th percentile tells us the deal amount below which 25%
#   of deals fall.
#
# - norm.cdf(x, mean, sd) returns P(X ≤ x).
#   Therefore:
#       P(3000 < X < 7000) = CDF(7000) - CDF(3000)
#       P(X > 1000) = 1 - CDF(1000)
#       P(X < 7500) = CDF(7500)
#
# Context:
# - norm is imported from scipy.stats
# - pandas is imported as pd
# - The DataFrame `amir_deals` contains monetary deal amounts but is not
#   directly needed since the distribution parameters are known.
# ============================================
