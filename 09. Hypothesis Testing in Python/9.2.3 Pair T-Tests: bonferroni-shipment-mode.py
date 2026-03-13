# ============================================
# 1. Task Description
# Identify which shipment modes have significantly different mean pack
# prices by running pairwise t-tests with a Bonferroni correction.
# This follows a one-way ANOVA that indicated at least one group mean
# difference.
#
# 2. Topics Covered
# - Pairwise t-tests with pingouin.pairwise_tests()
# - Multiple testing correction using Bonferroni adjustment
# - Interpreting pairwise comparison results
# ============================================

# 3. Python Script

# Modify the pairwise t-tests to use Bonferroni p-value adjustment
pairwise_results = pingouin.pairwise_tests(
    data=late_shipments,
    dv="pack_price",
    between="shipment_mode",
    padjust="bonf"
)

# Print pairwise_results
print(pairwise_results)

# ============================================
# 4. Additional Notes
# Pairwise t-tests
# - ANOVA only tells us that *some* group means differ, not *which* ones.
# - Pairwise t-tests compare every pair of shipment modes individually.
#
# Bonferroni correction:
# - Adjusts p-values to account for multiple comparisons.
# - This reduces the chance of false positives (Type I errors) by making
#   the test more conservative.
# - A comparison is considered significant if the adjusted p-value
#   ('p-corr') is below the chosen significance level (e.g., α = 0.10).
#
# Interpretation:
# - Each row in the output corresponds to a comparison between two
#   shipment modes.
# - Key columns to inspect:
#       • 'T'      → t-statistic
#       • 'p-unc'  → unadjusted p-value
#       • 'p-corr' → Bonferroni-corrected p-value
# - If 'p-corr' < α, the two shipment modes have significantly different
#   mean pack prices.
#
# Context:
# - `late_shipments` contains 'pack_price' and 'shipment_mode'.
# - pingouin is imported and provides both ANOVA and pairwise testing tools.
# ============================================
