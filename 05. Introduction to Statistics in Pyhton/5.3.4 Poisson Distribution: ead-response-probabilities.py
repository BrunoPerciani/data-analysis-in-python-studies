# ============================================
# 1. Task Description
# Using a Poisson distribution with λ = 4 (Amir responds to 4 leads per
# day on average), compute several probabilities:
# - P(X = 5): probability that Amir responds to exactly 5 leads.
# - P(X ≤ 2): probability that he responds to 2 or fewer leads.
# - P(X > 10): probability that he responds to more than 10 leads.
#
# 2. Topics Covered
# - Poisson distribution for count-based events
# - Probability mass function (PMF)
# - Cumulative distribution function (CDF)
# - Complement probabilities for “greater than” events
# ============================================

# 3. Python Script

# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of 5 responses
prob_5 = poisson.pmf(5, 4)
print(prob_5)

# Probability of 2 or fewer responses
prob_2_or_less = poisson.cdf(2, 4)
print(prob_2_or_less)

# Probability of > 10 responses
prob_over_10 = 1 - poisson.cdf(10, 4)
print(prob_over_10)

# ============================================
# 4. Additional Notes
# Tracking lead responses
# - Since lead responses are count-based events occurring over a fixed
#   period of time (a day), they follow a Poisson distribution.
# - The Poisson PMF gives P(X = k):
#       poisson.pmf(k, λ)
# - The Poisson CDF gives P(X ≤ k):
#       poisson.cdf(k, λ)
# - To compute P(X > k), use the complement:
#       1 - poisson.cdf(k, λ)
#
# In this scenario:
# - λ = 4 (Amir responds to 4 leads per day, on average)
# - P(X = 5) gives the chance of exactly five responses.
# - P(X ≤ 2) gives the chance of a very slow day.
# - P(X > 10) gives the probability of an unusually busy day.
#
# Context:
# - scipy.stats.poisson is imported
# - pandas and numpy are available but not required for this task
# ============================================
