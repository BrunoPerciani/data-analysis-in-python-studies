# ============================================
# 1. Task Description
# Compute a one-sided p-value for a hypothesis test on a population
# proportion using the standard normal (z) approximation. We test:
#   H0: p = 0.06
#   H1: p > 0.06
# given:
#   - late_prop_samp: observed sample proportion of late shipments
#   - late_prop_hyp: hypothesized proportion (0.06)
#   - std_error: bootstrap-based standard error estimate of the proportion
#
# 2. Topics Covered
# - Z-score for a sample proportion
# - One-sided p-value using the standard normal CDF
# - Interpreting p-values for hypothesis testing
# ============================================

# 3. Python Script

# Calculate the z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Calculate the one-sided (upper-tail) p-value for H1: p > p0
p_value = 1 - norm.cdf(z_score)

# Print the p-value
print(p_value)

# ============================================
# 4. Additional Notes
# Calculating p-values
# - For a "greater than" alternative (H1: p > p0), use the upper tail:
#       p-value = 1 - Φ(z)
#   where z = (estimate − hypothesized) / SE and Φ is the standard normal CDF.
# - A small p-value (e.g., < 0.05) suggests evidence against H0 in favor
#   of H1 (that the true late-shipment rate exceeds 6%).
#
# Assumptions & tips:
# - std_error here is estimated from the bootstrap distribution of the
#   sample proportion (preferred when normal approximation assumptions
#   are questionable or sample size/shape is complex).
# - If a two-sided test were needed, use:
#       p_two_sided = 2 * (1 - Φ(|z|))
#
# Context:
# - `late_prop_samp`, `late_prop_hyp` (= 0.06), and `std_error` are precomputed.
# - `norm` is imported from scipy.stats; pandas as pd and numpy as np are available.
# ============================================
