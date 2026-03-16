# ============================================
# 1. Task Description
# Use the Kruskal–Wallis test to determine whether the distribution of
# shipment weights differs across multiple shipment modes. This is a
# non-parametric alternative to one-way ANOVA that compares rank-based
# distributions without assuming normality.
#
# 2. Topics Covered
# - Non-parametric comparison across multiple groups
# - Kruskal–Wallis test using pingouin.kruskal()
# - Interpreting rank-based omnibus test results
# ============================================

# 3. Python Script

# Run a Kruskal-Wallis test on weight_kilograms vs. shipment_mode
kw_test = pingouin.kruskal(
    data=late_shipments,
    dv="weight_kilograms",
    between="shipment_mode"
)

# Print the results
print(kw_test)

# ============================================
# 4. Additional Notes
# Kruskal-Wallis
# - The Kruskal–Wallis test is the non-parametric counterpart to one-way
#   ANOVA and is appropriate when:
#       • Normality assumptions are violated
#       • There are outliers or skewed distributions
# - Hypotheses:
#       H0: All shipment_mode groups have the same distribution of weights.
#       H1: At least one shipment_mode group has a different distribution.
#
# Interpretation:
# - The test reports:
#       • H (chi-square-like statistic)
#       • p-value
#       • degrees of freedom
# - If p-value < α (e.g., 0.05 or 0.10), reject H0 and conclude that at
#   least one group differs.
#
# Next steps:
# - If H0 is rejected, follow up with pairwise non-parametric tests
#   (e.g., Dunn’s test with p-value adjustment) to identify which shipment
#   modes differ.
#
# Context:
# pandas is imported as pd, and pingouin provides the kruskal() function.
# The DataFrame `late_shipments` includes 'weight_kilograms' and
# 'shipment_mode'.
# ============================================
