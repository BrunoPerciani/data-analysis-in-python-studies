# ============================================
# 1. Task Description
# Identify non‑numeric columns in the planes dataset and count how many
# unique values each contains. This helps determine which categorical
# variables might need further cleaning, grouping, or reformatting.
#
# 2. Topics Covered
# - Selecting columns by data type using .select_dtypes()
# - Iterating over object (categorical/string) columns
# - Counting distinct values with .nunique()
# ============================================

# 3. Python Script

# Filter the DataFrame for object columns
non_numeric = planes.select_dtypes('object')

# Loop through columns
for col in non_numeric.columns:
    
    # Print the number of unique values
    print(f"Number of unique values in {col} column: ", non_numeric[col].nunique())

# ============================================
# 4. Additional Notes
# Finding the number of unique values
# - Object columns typically store text or mixed‑type data, often treated
#   as categorical features.
# - Columns with many unique values might:
#       • Contain IDs or free‑text fields  
#       • Require normalization or cleaning  
#       • Need to be excluded from certain analyses  
# - Columns with only a few categories may be suitable for:
#       • Grouping  
#       • Encoding (e.g., one‑hot or ordinal)  
#       • Aggregations  
#
# Context:
# pandas is imported as pd.
# The DataFrame `planes` contains numeric and non‑numeric columns.
# ============================================
