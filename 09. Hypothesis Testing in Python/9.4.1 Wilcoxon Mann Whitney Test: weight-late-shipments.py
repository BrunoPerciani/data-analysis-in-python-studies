# ============================================
# 1. Task Description
# Use a Wilcoxon–Mann–Whitney (WMW) test to assess whether the distribution
# of shipment weights differs between late and on-time deliveries. This
# non-parametric test compares the ranks of values rather than relying on
# distributional assumptions.
#
# 2. Topics Covered
# - Reshaping data with pivot() for group-wise comparison
# - Non-parametric hypothesis testing with pingouin.mwu()
# - Interpreting rank-based test results
# ============================================

# 3. Python Script

# Select the weight_kilograms and late columns
weight_vs_late = late_shipments[["weight_kilograms", "late"]]

# Convert weight_vs_late into wide format
weight_vs_late_wide = weight_vs_late.pivot(
    columns="late",
    values="weight_kilograms"
)

# Run a two-sided Wilcoxon-Mann-Whitney test on weight_kilograms vs. late
wmw_test = pingouin.mwu(
    x=weight_vs_late_wide["No"],
    y=weight_vs_late_wide["Yes"],
    alternative="two-sided"
)

# Print the test results
print(wmw_test)

# ============================================
# 4. Additional Notes
# Wilcoxon-Mann-Whitney
# - The WMW test is a rank-based alternative to the two-sample t-test.
# - It is appropriate when:
#       • Data are skewed or contain outliers
#       • Normality assumptions are questionable
# - Hypotheses (two-sided):
#       H0: The weight distributions for late and on-time shipments are the same.
#       H1: The weight distributions differ between the two groups.
#
# Interpretation:
# - The test compares the *ranks* of shipment weights rather than means.
# - A small p-value suggests a difference in distributions (often interpreted
#   as a difference in medians).
# - This test does not assume equal variances or normality.
#
# Context:
# pandas is imported as pd, and pingouin provides the mwu() function.
# The DataFrame `late_shipments` contains 'weight_kilograms' and 'late'.
# ============================================
