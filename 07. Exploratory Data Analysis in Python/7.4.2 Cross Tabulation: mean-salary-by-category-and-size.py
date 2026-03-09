# ============================================
# 1. Task Description
# Use cross-tabulation to explore how salaries vary across combinations
# of job category and company size in the salaries dataset. Compute the
# mean salary for each Job_Category × Company_Size combination using
# pd.crosstab() with an aggregation function.
#
# 2. Topics Covered
# - Cross-tabulation with pandas.crosstab()
# - Using values= and aggfunc= to compute aggregated metrics
# - Comparing salary patterns across multiple categorical variables
# ============================================

# 3. Python Script

# Cross-tabulate Job_Category and Company_Size
print(pd.crosstab(
    salaries["Job_Category"],
    salaries["Company_Size"],
    values=salaries["Salary_USD"],
    aggfunc="mean"
))

# ============================================
# 4. Additional Notes
# Cross-tabulation
# - pd.crosstab() is useful for examining how two categorical variables
#   intersect. By supplying:
#       values = salaries["Salary_USD"]
#       aggfunc = "mean"
#   the result becomes a matrix of **average salaries** for each category.
#
# Interpretation:
# - This allows you to inspect patterns such as whether certain job roles
#   earn more in larger companies, or whether specific company sizes tend
#   to pay more across categories.
#
# Tips:
# - You can change aggfunc to "median", "count", "std", or even custom
#   functions for deeper analysis.
# - Adding margins=True will append row/column totals or
