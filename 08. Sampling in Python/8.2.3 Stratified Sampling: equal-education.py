# ============================================
# 1. Task Description
# Create an equal-count stratified sample from the attrition population
# dataset by drawing the same number of observations from each Education
# subgroup. Then compute and display the subgroup proportions to confirm
# equal representation.
#
# 2. Topics Covered
# - Stratified sampling with equal sample size per group
# - Using groupby().sample(n=...) for fixed-number sampling
# - Checking subgroup proportions with value_counts(normalize=True)
# ============================================

# 3. Python Script

# Get 30 employees from each Education group
attrition_eq = attrition_pop.groupby("Education") \
    .sample(n=30, random_state=2022)

# Get the proportions from attrition_eq
education_counts_eq = attrition_eq["Education"].value_counts(normalize=True)

# Print the results
print(education_counts_eq)

# ============================================
# 4. Additional Notes
# Equal counts stratified sampling
# - Unlike proportional stratified sampling, equal-count sampling forces
#   each group (here, Education) to contribute *the same number* of
#   observations (30 per group).
# - This ensures perfect subgroup balance in the sample, regardless of
#   population size differences.
#
# Why use equal-count sampling?
# - Useful when:
#       • You want to avoid bias toward larger subgroups.
#       • You need balanced comparison across groups (e.g., modeling,
#         visualization, fairness checks).
# - But note:
#       • The resulting sample is *not representative* of subgroup sizes 
#         in the population.
#       • Use equal-count sampling when balance is more important than
#         representativeness.
#
# Context:
# pandas is loaded as pd.
# The DataFrame `attrition_pop` includes an "Education" column.
# ============================================
