# ============================================
# 1. Task Description
# Inspect a pandas DataFrame using core exploratory methods to quickly
# understand its structure and contents. The goal is to print the head,
# info, shape, and descriptive statistics of the dataset.
#
# 2. Topics Covered
# - DataFrame preview: .head()
# - Schema and types overview: .info()
# - Dimensions: .shape
# - Summary statistics: .describe()
# ============================================

# 3. Python Script

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())

# ============================================
# 4. Additional Notes
# Inspecting a DataFrame
# When you get a new DataFrame to work with, the first thing you need to do
# is explore it and see what it contains. There are several useful methods
# and attributes for this.
#
# - .head() returns the first few rows (the “head” of the DataFrame).
# - .info() shows information on each of the columns, such as the data type
#   and number of missing values.
# - .shape returns the number of rows and columns of the DataFrame.
# - .describe() calculates a few summary statistics for each column.
#
# Context:
# homelessness is a DataFrame containing estimates of homelessness in each
# U.S. state in 2018. The `individual` column is the number of homeless
# individuals not part of a family with children. The `family_members`
# column is the number of homeless individuals part of a family with children.
# The `state_pop` column is the state's total population.
#
# Note:
# pandas is imported for you and `homelessness` is assumed to be defined.
# ============================================
