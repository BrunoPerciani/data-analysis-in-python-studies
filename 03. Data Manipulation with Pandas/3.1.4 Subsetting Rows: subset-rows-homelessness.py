# ============================================
# 1. Task Description
# Subset rows of a DataFrame based on multiple conditions. The goal is to
# filter the homelessness dataset to include only rows where the number
# of family members is less than 1000 and the region is Pacific.
#
# 2. Topics Covered
# - Subsetting rows using relational operators
# - Filtering with multiple conditions
# - Using the bitwise AND operator (&) in pandas
# ============================================

# 3. Python Script

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[
    (homelessness["family_members"] < 1000) &
    (homelessness["region"] == "Pacific")
]

# See the result
print(fam_lt_1k_pac)

# ============================================
# 4. Additional Notes
# Subsetting rows
# A common part of data analysis is identifying which parts of a dataset
# match certain criteria. This process is known as filtering or selecting
# rows.
#
# You can filter a DataFrame by applying relational operators that return
# True or False for each row. These boolean results are then passed inside
# square brackets.
#
# Examples:
#     dogs[dogs["height_cm"] > 60]
#     dogs[dogs["color"] == "tan"]
#
# For multiple conditions, use the bitwise AND operator (&):
#     dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]
#
# In this exercise:
# - We filter for rows where family_members < 1000
# - AND region == "Pacific"
#
# Note:
# The DataFrame `homelessness` is assumed to be available and pandas is
# already imported as pd.
# ============================================
