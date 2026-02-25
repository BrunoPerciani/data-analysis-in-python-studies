# ============================================
# 1. Task Description
# Merge two DataFrames—taxi_owners and taxi_veh—on the shared column
# 'vid' using an inner join. Then identify the most common fuel_type
# used in Chicago taxis.
#
# 2. Topics Covered
# - Merging DataFrames with .merge()
# - Using suffixes to distinguish overlapping column names
# - Counting categorical values with .value_counts()
# - Exploring relationships between linked datasets
# ============================================

# 3. Python Script

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(
    taxi_veh,
    on="vid",
    suffixes=("_own", "_veh")
)

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh["fuel_type"].value_counts())

# ============================================
# 4. Additional Notes
# Your first inner join
# When two tables share a key column (here, 'vid'), merging them allows
# you to combine owner-level and vehicle-level information. Using an
# inner join ensures that only vid values present in both tables appear
# in the result.
#
# Steps performed:
# - taxi_owners.merge(taxi_veh, on="vid") joins matching taxi records.
# - suffixes=("_own", "_veh") prevents column name collisions.
# - .value_counts() reveals the frequency of each fuel_type.
#
# Context:
# pandas is preloaded as pd.
# DataFrames `taxi_owners` and `taxi_veh` are available.
# ============================================
