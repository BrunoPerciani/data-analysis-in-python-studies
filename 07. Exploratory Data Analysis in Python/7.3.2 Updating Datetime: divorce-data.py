# ============================================
# 1. Task Description
# Update the data type of the "marriage_date" column in the divorce
# DataFrame so that it is correctly stored as a DateTime object instead
# of a string. This conversion enables time‑based calculations and 
# temporal analysis in future steps.
#
# 2. Topics Covered
# - Converting string columns to datetime using pd.to_datetime()
# - Ensuring proper dtypes for date‑related analysis
# - Inspecting DataFrame dtypes
# ============================================

# 3. Python Script

# Convert the marriage_date column to DateTime values
divorce["marriage_date"] = pd.to_datetime(divorce["marriage_date"])

# (Optional) Check updated dtypes
print(divorce.dtypes)

# ============================================
# 4. Additional Notes
# Updating data type to DateTime
# - Some columns containing dates may be incorrectly imported as strings
#   (object dtype). These must be converted to datetime64[ns] to perform:
#       • date arithmetic (e.g., durations, ages, intervals)
#       • extraction of year, month, day
#       • chronological filtering and sorting
# - pd.to_datetime() safely parses common date formats and standardizes
#   them into pandas datetime objects.
#
# Context:
# pandas has been imported as pd.
# The DataFrame `divorce` contains a 'marriage_date' column that was
# originally stored as a string.
# ============================================
