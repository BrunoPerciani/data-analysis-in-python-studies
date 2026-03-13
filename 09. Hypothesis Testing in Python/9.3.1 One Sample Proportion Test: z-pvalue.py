# ============================================
# 1. Task Description
# Perform a one-sample z-test for a single proportion to assess whether
# the proportion of late shipments exceeds 6% (right-tailed test).
# Compute the z-score using the theoretical standard error based on the
# null hypothesis and return the corresponding p-value.
#
# 2. Topics Covered
# - One-sample proportion z-test
# - Theoretical standard error under H0
# - Right-tailed p-value via the standard normal CDF
# ============================================

# 3. Python Script

# Hypothesize that the proportion of late shipments is 6%
p_0 = 0.06

# Calculate the sample proportion of late shipments
p_hat = (late_shipments["late"] == "Yes").mean()

# Calculate the sample size
n = len(late_shipments)

# Calculate the numerator and denominator of the test statistic
numerator = p_hat - p_0
denominator = np.sqrt(p_0 * (1 - p_0) / n)

# Calculate the test statistic
z_score = numerator / denominator

# Calculate the p-value from the z-score (right-tailed test: H1: p > p0)
p_value = 1 - norm.cdf(z_score)

# Print the p-value
print(p_value)

# ============================================
# 4. Additional Notes
# Test for single proportions
# - Hypotheses:
#     H0: p = 0.06
#     H1: p > 0.06
# - Standard error under H0 (theoretical):
#     SE_H0 = sqrt( p0 * (1 - p0) / n )
# - Test statistic:
#     z = (p_hat − p0) / SE_H0
# - p-value (right tail):
#     p = 1 − Φ(z), where Φ is the standard normal CDF.
#
# Considerations:
# - This large-sample z-approximation works best when n*p0 and n*(1−p0)
#   are reasonably large (rule of thumb ≥ 10).
# - An alternative is to estimate the SE via bootstrap; both approaches
#   generally agree for sufficiently large samples and moderate proportions.
#
# Context:
# pandas (pd) and numpy (np) are available; `late_shipments` is loaded;
# `norm` is from scipy.stats.
# ============================================
