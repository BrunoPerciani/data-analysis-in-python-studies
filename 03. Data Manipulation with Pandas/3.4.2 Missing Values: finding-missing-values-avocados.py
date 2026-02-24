# ============================================
# 1. Task Description
# Detect and visualize missing values in the avocados_2016 dataset. The
# goal is to check for missing entries at both the element level and the
# column level, and to create a bar plot summarizing the number of
# missing values in each variable.
#
# 2. Topics Covered
# - Detecting missing values with .isna()
# - Checking if columns contain missing values using .any()
# - Summing missing values by column
# - Visualizing missing data using a bar plot
# ============================================

# 3. Python Script

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Finding missing values
# Missing values can interfere with calculations and visualizations.
# Before analyzing a dataset, it's essential to know where missing values
# occur and how many there are.
#
# Useful methods:
# - .isna() reveals missing values element-wise (True/False).
# - .isna().any() checks if a column contains at least one missing value.
# - .isna().sum() counts missing values per variable.
#
# Visualization:
# Plotting the counts as a bar chart helps you quickly identify which
# columns need cleaning or imputation.
#
# Context:
# pandas has been imported as pd.
# `avocados_2016` is a subset of the avocados dataset containing only
# sales records from 2016.
# ============================================
