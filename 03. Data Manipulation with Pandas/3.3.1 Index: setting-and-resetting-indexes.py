# ============================================
# 1. Task Description
# Explore how to set and reset indexes in a DataFrame. The goal is to
# practice assigning a column as the index and then restoring the default
# integer index, either keeping or discarding the original index values.
#
# 2. Topics Covered
# - Viewing a DataFrame
# - Setting a column as the index
# - Resetting the index with and without dropping it
# - Understanding how index operations affect the table structure
# ============================================

# 3. Python Script

# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index(drop=False))

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# ============================================
# 4. Additional Notes
# Setting and removing indexes
# pandas allows you to designate a column as an index. This can:
# - Make subsetting cleaner and more intuitive.
# - Improve performance for certain lookup operations.
#
# In this exercise:
# - We set "city" as the index using .set_index().
# - We reset the index twice:
#     * drop=False keeps the index as a regular column.
#     * drop=True discards the original index.
#
# Context:
# The DataFrame `temperatures` contains average temperatures for cities
# around the world. pandas has been imported as pd.
# ============================================
