# ============================================
# 1. Task Description
# Create a new DataFrame from a list of dictionaries. Each dictionary
# represents a row of avocado sales data for specific dates in 2019.
# The goal is to assemble the list into a structured DataFrame.
#
# 2. Topics Covered
# - Creating data using a list of dictionaries
# - Converting lists of dictionaries into a DataFrame
# - Inspecting the resulting DataFrame
# ============================================

# 3. Python Script

# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)

# ============================================
# 4. Additional Notes
# List of dictionaries
# A convenient way to build a DataFrame manually is by using a list of
# dictionaries. Each dictionary represents one row, and keys represent
# column names.
#
# Example:
#     [
#       {"date": "2019-11-03", "small_sold": 10376832, ...},
#       {"date": "2019-11-10", "small_sold": 10717154, ...},
#     ]
#
# This approach is useful when assembling small datasets by hand or when
# receiving row-wise JSON-like data.
#
# Context:
# pandas has been imported as pd.
# ============================================
