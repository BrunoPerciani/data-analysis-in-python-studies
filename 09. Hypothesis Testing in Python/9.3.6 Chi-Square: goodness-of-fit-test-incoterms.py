# ============================================
# 1. Task Description
# Perform a chi-square goodness of fit test to determine whether the
# observed distribution of vendor incoterms matches a hypothesized
# distribution. Use α = 0.10 to make a decision.
#
# 2. Topics Covered
# - Chi-square goodness of fit with scipy.stats.chisquare
# - Comparing observed vs. expected counts
# - Decision rule using a specified significance level
# ============================================

# 3. Python Script

# Perform a goodness of fit test on the incoterm counts n
gof_test = chisquare(
    f_obs=incoterm_counts["n"],
    f_exp=hypothesized["n"]
)

# Print gof_test results
print(gof_test)

# Optional: Decision at alpha = 0.10
alpha = 0.10
p_value = gof_test.pvalue

if p_value < alpha:
    print("Reject H0: The sample does not match the hypothesized distribution (α = 0.10).")
else:
    print("Fail to reject H0: No sufficient evidence against the hypothesized distribution (α = 0.10).")

# ============================================
# 4. Additional Notes
# Performing a goodness of fit test
# - Hypotheses:
#     H0: The observed incoterm distribution matches the hypothesized distribution.
#     H1: The observed distribution differs from the hypothesized distribution.
# - Inputs:
#     • f_obs: observed counts per category (incoterm_counts['n'])
#     • f_exp: expected counts per category derived from hypothesized proportions
# - Assumptions:
#     • Categories are mutually exclusive and collectively exhaustive.
#     • Expected counts are sufficiently large (rule of thumb ≥ 5).
# - Interpretation:
#     • If p-value < α, conclude that the observed distribution differs from the hypothesized one.
#     • Otherwise, we do not have sufficient evidence to claim a difference.
# ============================================
