# ============================================
# 1. Task Description
# Work with a nested dictionary (dictionary of dictionaries),
# where each country maps to another dictionary containing:
#   • its capital city
#   • its population (in millions)
#
# Tasks:
#   1. Access a nested value (the capital of France).
#   2. Create a new sub-dictionary for Italy.
#   3. Add it to the main europe dictionary.
#
# This exercise demonstrates multi-level dictionary access and updates.
#
# 2. Topics Covered
# - Nested dictionaries (dict of dicts)
# - Accessing nested elements with chained indexing
# - Adding new nested key:value structures
# ============================================

# 3. Python Script

# Dictionary of dictionaries
europe = {
    'spain':   {'capital': 'madrid', 'population': 46.77},
    'france':  {'capital': 'paris',  'population': 66.03},
    'germany': {'capital': 'berlin', 'population': 80.62},
    'norway':  {'capital': 'oslo',   'population': 5.084}
}

# Print out the capital of France (nested access)
print(europe['france']['capital'])

# Create sub-dictionary for Italy
data = {'capital': 'rome', 'population': 59.83}

# Add this nested dictionary to europe under key 'italy'
europe['italy'] = data

# Print the full nested dictionary
print(europe)

# ============================================
# 4. Additional Notes
# - Nested dictionaries allow for structured, multi-field data per key.
# - Access pattern:
#       europe['country']['field']
# - You can update nested values directly, e.g.:
#       europe['spain']['population'] = 47.0
# - To loop through nested dictionaries:
#       for country, info in europe.items():
#           print(country, info['capital'], info['population'])
# ============================================
