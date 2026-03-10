# ============================================
# 1. Task Description
# Perform proportional stratified sampling on the attrition population
# dataset based on the "Education" column. Compare the relative 
# frequencies of education levels in the population versus the stratified 
# sample to confirm proportional representation.
#
# 2. Topics Covered
# - Calculating subgroup proportions with value_counts(normalize=True)
# - Proportional stratified sampling using groupby().sample(frac=...)
# - Validating representativeness of samples
# ============================================

# 3. Python Script

# Proportion of employees by Education level
education_counts_pop = attrition_pop["Education"].value_counts(normalize=True)

# Print education_counts_pop
print(education_counts_pop)

# Proportional stratified sampling for 40% of each Education group
attrition_strat = (
    attrition_pop.groupby("Education")
    .sample(frac=0.4, random_state=2022)
)

# Calculate the Education level proportions from attrition_strat
education_counts_strat = attrition_strat["Education"].value_counts(normalize=True)

# Print education_counts_strat
print(education_counts_strat)

# ============================================
# 4. Additional Notes
# Proportional stratified sampling
# - Stratified sampling ensures that each subgroup (here, education level)
#   appears in the sample in the same proportion as in the population.
# - groupby("Education").sample(frac=0.4) draws 40% of rows from each
#   education category.
# - Comparing value_counts(normalize=True) for the population and the 
#   sample confirms representat
