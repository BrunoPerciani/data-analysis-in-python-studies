# ============================================
# 1. Task Description
# Clean and correct an existing dictionary of European countries
# and their capitals. Some entries are incorrect or unwanted:
#   • Germany has the wrong capital and needs to be updated.
#   • Australia does not belong in a Europe-focused dictionary
#     and should be removed.
# The task must be completed by manipulating the dictionary after
# creation, not by editing its initial definition.
#
# 2. Topics Covered
# - Updating dictionary values with assignment
# - Removing key–value pairs using del()
# - Printing dictionary contents
# ============================================

# 3. Python Script

# Definition of dictionary (intentionally contains incorrect entries)
europe = {
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'bonn',      # incorrect capital, must be fixed
    'norway': 'oslo',
    'italy': 'rome',
    'poland': 'warsaw',
    'australia': 'vienna'   # belongs outside Europe, must be removed
}

# Update capital of Germany
europe['germany'] = 'berlin'

# Remove Australia from the dictionary
del europe['australia']

# Print the corrected dictionary
print(europe)

# ============================================
# 4. Additional Notes
# - Updating a value is done via dictionary assignment:
#       europe['key'] = 'new_value'
# - Removing an entry can also be done with pop():
#       europe.pop('australia')
# - If a key might not exist, use:
#       europe.pop('australia', None)
#   to avoid KeyError.
# ============================================
