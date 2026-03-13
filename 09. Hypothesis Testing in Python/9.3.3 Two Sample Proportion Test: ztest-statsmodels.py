# ============================================
# 1. Task Description
# Use statsmodels' proportions_ztest() to test whether the proportion of
# late shipments differs between two freight cost groups ("expensive"
# vs. "reasonable"). Provide the counts of late shipments ("Yes") and
# total observations for each group, then compute the z statistic and
# one-sided p-value for H1: p_expensive > p_reasonable.
#
# 2. Topics Covered
# - Two-sample test for proportions
# - Using statsmodels.stats.proportion.proportions_ztest()
# - Constructing count and n arrays from grouped data
# ============================================

# 3. Python Script

# Count the late column values for each freight_cost_group
late_by_freight_cost_group = late_shipments.groupby("freight_cost_group")["late"].value_counts()

# Create an array of the "Yes" counts for each freight_cost_group
success_counts = np.array([45, 16])

# Create an array of the total number of rows in each freight_cost_group
n = np.array([45 + 500, 16 + 439])

# Run a z-test on the two proportions (right-tailed: H1: p_expensive > p_reasonable)
stat, p_value = proportions_ztest(
    count=success_counts,
    nobs=n,
    alternative="larger"
)

# Print the results
print(stat, p_value)

# ============================================
# 4. Additional Notes
# proportions_ztest() for two samples
# - Hypotheses (right‑tailed):
#     H0: p_expensive = p_reasonable
#     H1: p_expensive > p_reasonable
# - The function internally uses the pooled proportion under H0 and
#   computes a z statistic and corresponding p-value.
# - Inputs:
#     • count: array of success counts (e.g., number of "Yes" late shipments)
#     • nobs: array of total sample sizes for each group
# - If you need a two-sided test, use alternative="two-sided".
# - If you need H1: p_expensive < p_reasonable, use alternative="smaller".
#
# Context:
# - `late_shipments` contains 'freight_cost_group' and 'late' (Yes/No).
# - numpy is imported as np; proportions_ztest is from statsmodels.stats.proportion.
# ============================================
