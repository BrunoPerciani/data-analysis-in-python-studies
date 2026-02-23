# ============================================
# 1. Task Description
# Explore the internal components of a pandas DataFrame. The goal is to
# print the underlying NumPy values, the column index, and the row index
# of the dataset to understand how DataFrames are structured.
#
# 2. Topics Covered
# - Accessing raw data with .values
# - Accessing the column index with .columns
# - Accessing the row index with .index
# ============================================

# 3. Python Script

# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

# ============================================
# 4. Additional Notes
# Parts of a DataFrame
# A DataFrame consists of three main components, accessible as attributes:
#
# - .values: A two-dimensional NumPy array containing the underlying data.
# - .columns: An index object storing the DataFrame's column names.
# - .index: An index object storing the row labels (often integers or strings).
#
# Index objects can behave like lists, but they provide additional
# capabilities that will be explored later in the course.
#
# Note:
# The DataFrame `homelessness` is assumed to be available and already loaded.
# ============================================
