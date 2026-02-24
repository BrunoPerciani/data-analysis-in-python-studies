# ============================================
# 1. Task Description
# Replace missing values in selected numerical columns and visualize how
# this affects the distribution of the data using histograms. The goal is
# to compare the original distribution (with missing values) to the
# distribution after replacing missing values with zero.
#
# 2. Topics Covered
# - Visualizing missing values with histograms
# - Replacing missing values using .fillna()
# - Plotting multiple histograms at once
# - Understanding how imputation affects data distribution
# ============================================

# 3. Python Script

# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()

# ============================================
# 4. Additional Notes
# Replacing missing values
# Replacing missing values with a fixed number is another common way to
# handle missing data. For numerical columns, filling missing entries
# with zero is simple and effective, but it comes with assumptions.
#
# In this exercise:
# - Missing values in the sales columns are replaced with 0.
# - This assumes that missing sales values correspond to zero units sold.
# - Plotting histograms before and after filling helps visualize how the
#   distribution changes due to imputation.
#
# Tips:
# - Use .hist() on multiple columns to generate multiple plots at once.
# - Be cautious: filling missing values can bias averages and totals.
#
# Context:
# pandas has been imported as pd.
# matplotlib.pyplot has been imported as plt.
# `avocados_2016` is available and contains some missing values.
# ============================================
