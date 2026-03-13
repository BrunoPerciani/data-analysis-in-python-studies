# ============================================
# 1. Task Description
# Compute the two-sample t test statistic to assess whether there is a
# difference in mean shipment weight between on-time (late == "No") and
# late (late == "Yes") deliveries. The test statistic is:
#
#        t = (x̄_no − x̄_yes) / sqrt( s_no² / n_no + s_yes² / n_yes )
#
# 2. Topics Covered
# - Two-sample t-statistic (unequal variances, Welch's t)
# - Combining sample means, standard deviations, and sizes
# - Preparing for hypothesis testing on mean differences
# ============================================

# 3. Python Script

# Calculate the numerator of the test statistic
numerator = xbar_no - xbar_yes

# Calculate the denominator of the test statistic
denominator = np.sqrt(s_no ** 2 / n_no + s_yes ** 2 / n_yes)

# Calculate the test statistic
t_stat = numerator / denominator

# Print the test statistic
print(t_stat)

# ============================================
# 4. Additional Notes
# Two sample mean test statistic
# - This formulation corresponds to Welch’s two-sample t-test, which does
#   not assume equal population variances.
# - A positive t_stat indicates x̄_no > x̄_yes; a negative value indicates
#   the opposite. The magnitude reflects how many standard errors separate
#   the two sample means.
# - To complete the test, compute the approximate degrees of freedom
#   (Welch–Satterthwaite) and then obtain a p-value from the t-distribution,
#   choosing one- or two-sided alternatives as appropriate to your question.
#
# Context:
# - xbar_no, s_no, n_no: mean, std dev, and size for on-time shipments.
# - xbar_yes, s_yes, n_yes: mean, std dev, and size for late shipments.
# - numpy is imported as np.
# ============================================
