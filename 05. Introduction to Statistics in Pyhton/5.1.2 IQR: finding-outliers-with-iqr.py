# ============================================
# 1. Task Description
# Use the Interquartile Range (IQR) method to identify outliers in the
# distribution of total CO₂ emissions per country. Compute country-level
# totals, derive Q1, Q3, and IQR, then flag observations outside the
# [Q1 - 1.5*IQR, Q3 + 1.5*IQR] range.
#
# 2. Topics Covered
# - Grouping and summing with .groupby()
# - Quantile calculations with numpy
# - IQR-based outlier detection
# - Boolean subsetting of a Series
# ============================================

# 3. Python Script

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby("country")["co2_emission"].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[
    (emissions_by_country > upper) |
    (emissions_by_country < lower)
]
print(outliers)

# ============================================
# 4. Additional Notes
# Finding outliers using IQR
# Outliers can distort mean-based statistics (mean, variance, std). The
# IQR method is more robust because it relies on quartiles (Q1 and Q3).
# A data point is considered an outlier if it lies below:
#     Q1 - 1.5 * IQR
# or above:
#     Q3 + 1.5 * IQR
#
# Context:
# - pandas is imported as pd
# - numpy is imported as np
# - The DataFrame `food_consumption` contains 'country' and 'co2_emission'.
#
# Notes:
# - You can adjust the multiplier (1.5) to be more or less conservative.
# - Consider inspecting both high and low outliers separately, depending
#   on your analysis goals.
# ============================================
