# ============================================
# 1. Task Description
# Generate a simple random sample (SRS) of 100 employees from the
# attrition population dataset, compute the sample mean of Attrition,
# and calculate the relative error (%) versus the population mean.
#
# 2. Topics Covered
# - Simple random sampling with pandas .sample()
# - Computing sample means
# - Relative error as an accuracy metric for point estimates
# ============================================

# 3. Python Script

# Generate a simple random sample of 100 rows, with seed 2022
attrition_srs100 = attrition_pop.sample(n=100, random_state=2022)

# Calculate the mean employee attrition in the sample
mean_attrition_srs100 = attrition_srs100["Attrition"].mean()

# Calculate the relative error percentage
rel_error_pct100 = 100 * abs(mean_attrition_pop - mean_attrition_srs100) / mean_attrition_pop

# Print rel_error_pct100
print(rel_error_pct100)

# ============================================
# 4. Additional Notes
# Calculating relative errors
# - Relative error (%) compares how far a sample estimate is from the true
#   population parameter:
#       Relative Error = |μ_pop − x̄_sample| / μ_pop × 100
# - Smaller relative error indicates the sample mean is closer to the
#   population mean, which is more likely with larger samples (by CLT).
#
# Context:
# - pandas is imported as pd.
# - `attrition_pop` is the full population DataFrame.
# - `mean_attrition_pop` is the population mean of the 'Attrition' column
#   computed beforehand (e.g., attrition_pop['Attrition'].mean()).
# ============================================
