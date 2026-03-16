# ============================================
# 1. Task Description
# Examine whether the distribution of freight cost groups ("expensive",
# "reasonable") depends on the vendor incoterms (EXW, CIP, DDP, FCA).
# Visualize proportional distributions using a stacked bar chart and
# perform a chi-square test of independence at α = 0.01.
#
# 2. Topics Covered
# - Groupby proportions and reshaping with .unstack()
# - Proportional stacked bar chart for two categorical variables
# - Chi-square test of independence with pingouin.chi2_independence()
# - Interpreting p-values against a specified significance level
# ============================================

# 3. Python Script

# Proportion of freight_cost_group grouped by vendor_inco_term
props = late_shipments.groupby("vendor_inco_term")["freight_cost_group"].value_counts(normalize=True)

# Convert props to wide format
wide_props = props.unstack()

# Proportional stacked bar plot of freight_cost_group vs. vendor_inco_term
wide_props.plot(kind="bar", stacked=True)
plt.show()

# Determine if freight_cost_group and vendor_inco_term are independent
expected, observed, stats = pingouin.chi2_independence(
    data=late_shipments,
    x="vendor_inco_term",
    y="freight_cost_group"
)

# Print Pearson chi-square line
print(stats[stats["test"] == "pearson"])

# Optional: Decision at alpha = 0.01
alpha = 0.01
pearson_p = stats.loc[stats["test"] == "pearson", "pval"].iloc[0]
if pearson_p < alpha:
    print("Reject H0: Evidence that vendor_inco_term and freight_cost_group are associated (α = 0.01).")
else:
    print("Fail to reject H0: No sufficient evidence of association at α = 0.01.")

# ============================================
# 4. Additional Notes
# Performing a chi-square test
# - H0: vendor_inco_term and freight_cost_group are independent.
# - H1: vendor_inco_term and freight_cost_group are associated.
#
# What to look at in 'stats':
# - 'chi2'  → Pearson chi-square statistic
# - 'dof'   → degrees of freedom
# - 'pval'  → p-value for the independence test
#
# Visualization:
# - The stacked bar chart helps you compare proportions of "expensive"
#   vs. "reasonable" across each incoterm category. Visual differences
#   suggest possible dependence; the chi-square test formalizes this.
#
# Assumptions:
# - Sufficiently large expected counts in each cell (rule of thumb ≥ 5).
# - Independent observations.
# ============================================
