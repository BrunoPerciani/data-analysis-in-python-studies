# ============================================
# 1. Task Description
# Calculate a 95% confidence interval for the population mean popularity
# using two methods:
#   (1) The bootstrap quantile method
#   (2) The standard error method using the inverse CDF (norm.ppf)
#
# 2. Topics Covered
# - Bootstrap confidence intervals (percentile/quantile method)
# - Standard error method for confidence intervals
# - Using scipy.stats.norm to compute z-values
# ============================================

# 3. Python Script

# Generate a 95% confidence interval using the quantile method
lower_quant = np.quantile(bootstrap_distribution, 0.025)
upper_quant = np.quantile(bootstrap_distribution, 0.975)

# Print quantile method confidence interval
print((lower_quant, upper_quant))

# Standard error method
# Compute the standard deviation of the bootstrap distribution (bootstrap SE)
boot_sd = np.std(bootstrap_distribution, ddof=1)

# Compute the standard error for the statistic (mean popularity)
se_boot = boot_sd

# Lower and upper bounds using z = 1.96 for 95% CI
lower_se = np.mean(bootstrap_distribution) - norm.ppf(0.975) * se_boot
upper_se = np.mean(bootstrap_distribution) + norm.ppf(0.975) * se_boot

# Print SE method confidence interval
print((lower_se, upper_se))

# ============================================
# 4. Additional Notes
# Calculating confidence intervals
# - Quantile (percentile) method:
#       CI = [quantile(0.025), quantile(0.975)]
#   This uses the empirical bootstrap distribution directly, making no
#   assumptions about normality.
#
# - Standard error method:
#       CI = mean ± z * SE
#   where z = 1.96 for a 95% CI and SE is estimated from the bootstrap.
#   This method assumes the bootstrap distribution of the statistic is
#   approximately normal.
#
# Interpretation:
# - If the bootstrap distribution is symmetric and bell-shaped, the
#   quantile and SE methods will be similar.
# - If the bootstrap distribution is skewed, the quantile method is
#   generally more reliable.
#
# Context:
# spotify_population, spotify_sample, and bootstrap_distribution are available.
# pandas and numpy are imported; norm is imported from scipy.stats.
