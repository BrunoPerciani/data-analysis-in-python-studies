# ============================================
# 1. Task Description
# Convert two parallel lists of countries and capitals into a dictionary
# where each country is a key and its corresponding capital is the value.
# This exercise reinforces basic Python dictionary creation and key‑value
# mapping.
#
# 2. Topics Covered
# - List-to-dictionary conversion
# - Dictionary literals in Python
# - Key–value structure and basic dictionary usage
# ============================================

# 3. Python Script

# Definition of countries and capitals lists
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From strings in countries and capitals, create dictionary 'europe'
# Using explicit key-value pairs
europe = {
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'berlin',
    'norway': 'oslo'
}

# Print the resulting dictionary
print(europe)

# ============================================
# 4. Additional Notes
# - A more general solution could use zip():
#       europe = dict(zip(countries, capitals))
# - Dictionary keys must be unique; if duplicates appear, later values overwrite earlier ones.
# ============================================
