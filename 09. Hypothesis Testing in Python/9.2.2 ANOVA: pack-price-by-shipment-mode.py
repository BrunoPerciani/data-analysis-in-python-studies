# ============================================
# 1. Task Description
# Test whether the mean pack price differs across shipment modes using a
# one-way ANOVA. Evaluate the result at a significance level of α = 0.10.
#
# 2. Topics Covered
# - One-way ANOVA with pingouin.anova()
# - Interpreting ANOVA results (F-statistic, p-value)
# - Automated decision at a specified alpha level
# ============================================

# 3. Python Script

# Run an ANOVA for pack_price across shipment_mode
anova_results = pingouin.anova(
    data=late_shipments,
    dv="pack_price",
    between="shipment_mode"
)

# Print anova_results
print(anova_results)

# Decision at alpha = 0.10
alpha = 0.10
p_value = anova_results["p-unc"].iloc[0]

if p_value < alpha:
    print("Reject H0: Evidence that at least one shipment mode has a different mean pack price.")
else:
    print("Fail to reject H0: No sufficient evidence of mean differences across shipment modes at α = 0.10.")

# ============================================
# 4. Additional Notes
# Conducting an ANOVA test
# - H0: Mean pack prices are equal across all shipment modes.
# - H1: At least one shipment mode has a different mean pack price.
# - ANOVA reports an F-statistic and an uncorrected p-value ('p-unc').
#   If p < α, we reject H0 and conclude that some group means differ.
# - If H0 is rejected, consider post-hoc comparisons (e.g., Tukey HSD)
#   to identify which pairs of modes differ.
#
# Assumptions:
# - Independent observations across shipment_mode groups.
# - Approximately normal distribution of residuals within each group.
# - Homogeneity of variances across groups (can be checked with Levene's test).
# ============================================
