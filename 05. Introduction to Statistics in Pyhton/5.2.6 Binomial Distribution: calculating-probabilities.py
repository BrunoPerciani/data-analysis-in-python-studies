# ============================================
# 1. Task Description
# Calculate binomial probabilities for Amir’s weekly sales performance,
# assuming he works on 3 deals per week and wins 30% of them. Compute:
# - The probability of closing all 3 deals.
# - The probability of closing more than 1 deal.
#
# 2. Topics Covered
# - Binomial probability mass function (PMF)
# - Binomial cumulative distribution function (CDF)
# - Computing P(X = k) and P(X > k)
# ============================================

# 3. Python Script

# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3, 3, 0.3)
print(prob_3)

# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = binom.cdf(3, 3, 0.3) - binom.cdf(1, 3, 0.3)
print(prob_greater_than_1)

# ============================================
# 4. Additional Notes
# Calculating binomial probabilities
# - PMF (probability mass function) gives P(X = k) for a Binomial(n, p)
#   distribution.
# - CDF (cumulative distribution function) gives P(X ≤ k).
#
# Here:
# - n = 3 deals per week
# - p = 0.30 probability of winning each deal
#
# Thus:
# - P(X = 3) is computed with binom.pmf(3, 3, 0.3)
# - P(X > 1) = P(X ≤ 3) – P(X ≤ 1)
#
# Context:
# scipy.stats.binom is imported, and no DataFrame is required for this task.
# ============================================
