# ============================================
# 1. Task Description
# Use merge_asof() to align quarterly GDP values with recession status
# (based on start/stop periods) and create a visual flag indicating
# whether each quarter falls in a recession. Finally, plot a bar chart
# of GDP colored by economic status.
#
# 2. Topics Covered
# - Time-aware joins with pd.merge_asof()
# - Creating categorical flags from joined data
# - Plotting time series as a colored bar chart
# ============================================

# 3. Python Script

# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on="date")

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ["r" if s == "recession" else "g" for s in gdp_recession["econ_status"]]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind="bar", y="gdp", x="date", color=is_recession, rot=90)
plt.show()

# ============================================
# 4. Additional Notes
# Using merge_asof() to create dataset
# merge_asof() aligns observations by nearest time key and is useful when
# series are reported at different frequencies or on non-matching dates.
# After merging, we map the 'econ_status' to colors:
# - 'r' (red) for recession quarters
# - 'g' (green) for growth quarters
#
# Context:
# The DataFrames `gdp` (quarterly GDP, with 'date' and 'gdp') and
# `recession` (with 'date' and 'econ_status') are available.
# pandas is imported as pd, matplotlib.pyplot as plt.
# ============================================
