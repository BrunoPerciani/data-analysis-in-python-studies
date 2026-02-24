# ============================================
# 1. Task Description
# Remove rows containing missing values from a DataFrame. The goal is to
# create a clean version of the dataset in which all columns contain only
# complete (non-missing) observations.
#
# 2. Topics Covered
# - Removing missing values with .dropna()
# - Checking for remaining missing values with .isna().any()
# - Creating a fully complete subset of a dataset
# ============================================

# 3. Python Script

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())

# ============================================
# 4. Additional Notes
# Removing missing values
# Once missing values are identified in a dataset, one approach to
# handling them is to remove the rows that contain them entirely.
# This is done with .dropna().
#
# Key points:
# - .dropna() removes rows that contain *any* missing values.
# - After dropping missing values, use .isna().any() to verify that the
#   resulting dataset is fully complete.
#
# Considerations:
# - Dropping missing values can reduce the size of your dataset.
# - In some analyses, imputation (filling missing values) may be preferred.
#
# Context:
# pandas has been imported as pd.
# `avocados_2016` is available and may contain missing values.
# ============================================
