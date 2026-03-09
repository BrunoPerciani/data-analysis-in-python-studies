# ============================================
# 1. Task Description
# Compare the distribution of job categories in the salaries dataset to
# the known population distribution from the 2022 Kaggle Survey. Compute
# the relative frequency of each job category to check whether the sample
# is representative or imbalanced.
#
# 2. Topics Covered
# - Calculating relative frequencies with .value_counts(normalize=True)
# - Inspecting class balance in categorical variables
# - Comparing sample vs. population distributions
# ============================================

# 3. Python Script

# Print the relative frequency of Job_Category
print(salaries["Job_Category"].value_counts(normalize=True))

# ============================================
# 4. Additional Notes
# Checking for class imbalance
# - value_counts(normalize=True) returns proportions instead of raw counts.
# - Comparing these proportions to the Kaggle population distribution
#   helps determine whether the salaries dataset over‑ or under‑represents
#   certain job categories.
#
# For reference, Kaggle Survey 2022 relative frequencies:
#   Data Science:      0.281236
#   Data Analytics:    0.224231
#   Other:             0.214609
#   Managerial:        0.121300
#   Machine Learning:  0.083248
#   Data Engineering:  0.075375
#
# Interpretation:
# - If a category in salaries differs greatly from these baseline
#   proportions, the sample may be imbalanced.
# - Class imbalance can affect:
#       • statistical conclusions  
#       • visualizations  
#       • model training (bias toward majority class)  
#
# Context:
# pandas has been imported as pd.
# The DataFrame `salaries` contains a 'Job_Category' column to analyze.
# ============================================
