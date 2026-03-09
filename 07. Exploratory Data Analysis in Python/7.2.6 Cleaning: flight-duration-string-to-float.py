# ============================================
# 1. Task Description
# Clean the "Duration" column in the planes dataset so it can be analyzed
# numerically. The raw column contains string values ending in "h".
# Remove the string character and convert the column to a float, then
# visualize the distribution of flight durations with a histogram.
#
# 2. Topics Covered
# - Previewing raw string data
# - Cleaning text columns with .str.replace()
# - Converting string data to numeric types
# - Plotting distributions with seaborn.histplot()
# ============================================

# 3. Python Script

# Preview the column
print(planes["Duration"].head())

# Remove the string character
planes["Duration"] = planes["Duration"].str.replace("h", "")

# Convert to float data type
planes["Duration"] = planes["Duration"].astype(float)

# Plot a histogram
sns.histplot(x="Duration", data=planes)
plt.show()

# ============================================
# 4. Additional Notes
# Flight duration
# - The raw string values (e.g., "2h", "15h") need to be cleaned before
#   numerical analysis.
# - .str.replace("h", "") strips the trailing "h" so that only the hour
#   number remains.
# - Converting to float enables statistical analysis, visualization,
#   aggregations, and comparisons between flights.
#
# Caveats:
# - Some durations include minutes (e.g., "5h 25m"). These will not 
#   convert cleanly with this simple method and may generate errors or
#   NaN values depending on pandas behavior. A more robust cleaning step
#   using regex is needed for full parsing.
# - For strictly hour‑based durations shown here, this approach works
#   correctly.
#
# Context:
# pandas as pd, numpy as np, seaborn as sns, and matplotlib.pyplot as plt
# are available. The DataFrame `planes` contains a "Duration" column
# with string values.
# ============================================
