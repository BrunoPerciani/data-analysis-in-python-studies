# ============================================
# 1. Task Description
# Compute a z-score for the proportion of late shipments by standardizing
# the difference between the sample proportion and a hypothesized
# population proportion using the bootstrap-based standard error.
#
# 2. Topics Covered
# - Standardization and z-scores
# - Bootstrap standard error for a proportion
# - Hypothesis testing setup for proportions
# ============================================

# 3. Python Script

late_prop_hyp = 0.06

# Calculate the standard error
std_error = np.std(late_shipments_boot_distn, ddof=1)

# Find z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Print z_score
print(z_score)

# ============================================
# 4. Additional Notes
# Calculating a z-score
# - The z-score standardizes a statistic relative to its standard error:
#       z = (estimate − hypothesized_value) / SE
# - Here, the estimate is the sample proportion of late shipments
#   (late_prop_samp), the hypothesized value is 0.06, and the SE is
#   estimated from the bootstrap distribution of the proportion
#   (late_shipments_boot_distn).
# - A larger |z| indicates stronger evidence against the null hypothesis
#   under normal approximation assumptions for the standardized statistic.
#
# Context:
# - `late_shipments` was previously explored to compute late_prop_samp.
# - `late_shipments_boot_distn` is a bootstrap distribution (list/array)
#   of resampled proportions for late shipments.
# - pandas as pd and numpy as np are available.
# ============================================
