# ============================================
# 1. Task Description
# Explore how weighted sampling influences the distribution of YearsAtCompany
# when drawing a sample from the attrition population. First visualize the
# population distribution, then generate a weighted sample where the
# probability of selecting each employee is proportional to their
# YearsAtCompany, and compare the resulting distribution.
#
# 2. Topics Covered
# - Histogram visualization for numeric variables
# - Weighted random sampling with pandas .sample(weights=...)
# - Comparing sample vs. population distributions
# ============================================

# 3. Python Script

# Plot YearsAtCompany from attrition_pop as a histogram
attrition_pop["YearsAtCompany"].hist(bins=np.arange(0, 41, 1))
plt.show()

# Sample 400 employees weighted by YearsAtCompany
attrition_weight = attrition_pop.sample(
    n=400,
    weights="YearsAtCompany"
)

# Plot YearsAtCompany from attrition_weight as a histogram
attrition_weight["YearsAtCompany"].hist(bins=np.arange(0, 41, 1))
plt.show()

# ============================================
# 4. Additional Notes
# Weighted sampling
# - Weighted sampling allows certain rows to have a higher probability of
#   being selected based on the value in a chosen column.
# - In this example, employees with more YearsAtCompany have a larger
#   probability of being sampled.
# - This results in a sample distribution that over-represents employees
#   with longer tenure compared to simple random sampling.
#
# Why use weighted sampling?
# - Helpful when:
#       • You want to emphasize underrepresented but important cases.
#       • You want to model or analyze data at a different weighting than
#         what naturally occurs in the dataset.
#
# Notes:
# - If any row has a weight of 0, it will never be selected.
# - If weights contain NaN, pandas will raise an error unless handled.
#
# Context:
# pandas is loaded as pd,
# numpy as np,
# matplotlib.pyplot as plt.
# The DataFrame `attrition_pop` includes 'YearsAtCompany'.
# ============================================
