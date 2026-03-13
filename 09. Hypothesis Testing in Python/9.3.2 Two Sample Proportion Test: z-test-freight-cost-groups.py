# ============================================
# 1. Task Description
# Perform a two-proportions z-test to assess whether the late-shipment
# rate differs between freight cost groups ("expensive" vs "reasonable").
# Compute the pooled proportion, standard error under H0, z-score, and
# the one-sided p-value for H1: p_expensive > p_reasonable.
#
# 2. Topics Covered
# - Two-proportions z-test
# - Pooled proportion under H0
# - Standard error for difference in proportions
# - One-sided p-value using the standard normal CDF
# ============================================

# 3. Python Script

# Calculate the pooled estimate of the population proportion
p_hat = (
    p_hats["reasonable"] * ns["reasonable"]
    + p_hats["expensive"] * ns["expensive"]
) / (ns["reasonable"] + ns["expensive"])

# Calculate p_hat one minus p_hat
p_hat_times_not_p_hat = p_hat * (1 - p_hat)

# Divide this by each of the sample sizes and then sum
p_hat_times_not_p_hat_over_ns = (
    p_hat_times_not_p_hat / ns["expensive"]
    + p_hat_times_not_p_hat / ns["reasonable"]
)

# Calculate the standard error
std_error = np.sqrt(p_hat_times_not_p_hat_over_ns)

# Calculate the z-score (difference in sample proportions)
z_score = (p_hats["expensive"] - p_hats["reasonable"]) / std_error

# Calculate the p-value from the z-score (right-tailed: H1: p_expensive > p_reasonable)
p_value = 1 - norm.cdf(z_score)

# Print p_value
print(p_value)

# ============================================
# 4. Additional Notes
# Test of two proportions
# - Hypotheses (right-tailed):
#     H0: p_expensive = p_reasonable
#     H1: p_expensive > p_reasonable
# - Pooled proportion under H0:
#     p̂ = (x1 + x2) / (n1 + n2),
#   equivalently computed here using p_hats and ns.
# - Standard error under H0:
#     SE = sqrt( p̂(1 − p̂)(1/n1 + 1/n2) )
# - Test statistic:
#     z = (p̂1 − p̂2) / SE
# - p-value (right tail):
#     p = 1 − Φ(z)
#
# Interpretation:
# - A small p-value (e.g., < 0.05 or chosen α) provides evidence that the
#   late-shipment proportion for
