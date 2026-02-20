# ============================================
# 1. Task Description
# Access values stored inside a Python dictionary. Given a dictionary
# mapping European countries to their capitals, retrieve:
#   • the full list of dictionary keys
#   • the capital of Norway by using the key 'norway'
#
# This exercise reinforces basic dictionary access syntax.
#
# 2. Topics Covered
# - Dictionary key access (my_dict[key])
# - Retrieving all keys with .keys()
# - Understanding key–value lookup
# ============================================

# 3. Python Script

# Definition of dictionary
europe = {
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'berlin',
    'norway': 'oslo'
}

# Print out the keys in europe
print(europe.keys())

# Print out the value that belongs to key 'norway'
print(europe['norway'])

# ============================================
# 4. Additional Notes
# - europe.keys() returns a "dict_keys" view; you can convert to a list:
#       list(europe.keys())
# - Accessing a non-existing key (e.g., europe['italy']) will raise KeyError.
#   Use europe.get('italy') to return None instead.
# ============================================
