# ============================================
# 1. Task Description
# Detect and fix incorrect data types in the unemployment dataset. One
# of the columns was stored as the wrong type, preventing proper numeric
# analysis. Convert the 2019 column to a float and verify the correction.
#
# 2. Topics Covered
# - Detecting incorrect dtypes using .dtypes
# - Converting column types using .astype()
# - Ensuring numeric columns are ready for analysis
# ============================================

# 3. Python Script

# Update the data type of the 2019 column to a float
unemployment["2019"] = unemployment["2019"].astype(float)

# Print the dtypes to check your work
print(unemployment.dtypes)

# ============================================
# 4. Additional Notes
# Detecting data types
# - Incorrect data types (e.g., numeric values stored as strings) often
#   block calculations, visualizations, summaries, and merges.
# - unemployment.dtypes helps quickly identify which columns have invalid
#   formats.
# - .astype(float) ensures the 2019 unemployment values are numeric and
#   ready for analysis (e.g., computing means, correlations, or trends).
#
# Context:
# pandas is imported as pd.
# The DataFrame `unemployment` is already loaded.
# ============================================
