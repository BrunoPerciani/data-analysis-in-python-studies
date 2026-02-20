# ============================================
# 1. Task Description
# Loop over a dictionary containing European countries and their 
# capitals. For each key–value pair, print a formatted sentence 
# describing the capital of each country.
#
# 2. Topics Covered
# - Iterating over dictionaries with .items()
# - Accessing keys and values
# - String concatenation and formatting
# ============================================

# 3. Python Script

# Definition of dictionary
europe = {
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'berlin',
    'norway': 'oslo',
    'italy': 'rome',
    'poland': 'warsaw',
    'austria': 'vienna'
}

# Iterate over dictionary items and print country–capital pairs
for key, value in europe.items():
    print("the capital of " + str(key) + " is " + str(value))

# ============================================
# 4. Additional Notes
# - Using `.items()` returns (key, value) tuples.
# - You can use f-strings for cleaner formatting:
#       print(f"The capital of {key} is {value}")
# - Dictionaries preserve insertion order in Python 3.7+.
# ============================================
