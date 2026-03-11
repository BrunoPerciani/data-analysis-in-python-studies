# ============================================
# 1. Task Description
# Calculate a 95% confidence interval for a mean using the standard error
# method based on a bootstrap distribution. Specifically:
# - Compute the bootstrap point estimate (mean of bootstrap_distribution)
# - Compute the bootstrap standard error (std of bootstrap_distribution)
# - Use the inverse CDF (norm.ppf) to get the 2.5% and 97.5% bounds
#
# 2. Topics Covered
# - Bootstrap-based standard error of a statistic
# - Confidence intervals via the standard error method
# - Using scipy.stats.norm.ppf for inverse CDF calculations
# ============================================

# 3. Python Script

# Find the mean and std dev of the bootstrap distribution
point_estimate = np.mean(bootstrap_distribution)
standard_error = np.std(bootstrap_distribution, ddof=1)

# Find the lower limit of the confidence interval
lower_se = norm.ppf(0.025, loc=point_estimate, scale=standard_error)

# Find the upper limit of the confidence interval
upper_se = norm.ppf(0.975, loc=point_estimate, scale=standard_error)

# Print standard error method confidence interval
print((lower_se, upper_se))

# ============================================
# 4. Additional Notes
# Calculating confidence intervals
# - Standard error method:
#     CI_95% = mean_bootstrap ± z_(0.975) * SE_bootstrap
#   where z_(0.975) ≈ 1.96 for a 95% CI and SE_bootstrap is the standard
#   deviation of the bootstrap distribution.
# - This assumes the bootstrap distribution of the statistic is
#   approximately normal. If the bootstrap distribution is skewed,
#   prefer the percentile (quantile) method:
#       (np.quantile(bootstrap_distribution, 0.025),
#        np.quantile(bootstrap_distribution, 0.975))
#
# Context:
# - `bootstrap_distribution` contains many bootstrap replicates of the
#   statistic of interest (e.g., mean popularity).
# - `norm` is imported from scipy.stats; numpy as np is available.
# ============================================
