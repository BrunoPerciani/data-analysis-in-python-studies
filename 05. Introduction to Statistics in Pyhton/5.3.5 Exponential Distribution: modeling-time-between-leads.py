# ============================================
# 1. Task Description
# Model the time it takes Amir to respond to a sales lead using an
# exponential distribution. On average, Amir responds to one lead every
# 2.5 hours. Compute the probabilities that a response time:
# - Falls between 3 and 4 hours
# - Is greater than 4 hours
# - Is less than 1 hour
#
# 2. Topics Covered
# - Exponential distribution for modeling time between events
# - Using expon.cdf() to compute probabilities
# - Interval, upper-tail, and lower-tail probability calculations
# ============================================

# 3. Python Script

# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes 3-4 hours
print(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5))

# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes > 4 hours
print(1 - expon.cdf(4, scale=2.5))

# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes < 1 hour
print(expon.cdf(1, scale=2.5))

# ============================================
# 4. Additional Notes
# Modeling time between leads
# - When responses occur randomly in time at a constant average rate
#   (1 every 2.5 hours), the exponential distribution is appropriate.
# - scale = mean time between events → here, scale = 2.5 hours.
#
# Mathematical forms:
# - P(a < X < b) = CDF(b) – CDF(a)
# - P(X > t) = 1 – CDF(t)
# - P(X < t) = CDF(t)
#
# Interpretation:
# - Short response times are more likely than long ones due to the
#   exponential's right-skewed shape.
#
# Context:
# norm, poisson, and previous distributions are not needed here.
# Only scipy.stats.expon, pandas, numpy, and matplotlib are available.
# ============================================
