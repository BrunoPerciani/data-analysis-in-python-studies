# ============================================
# 1. Task Description
# Create a scatter plot to visualize GDP per capita against life
# expectancy for various countries in 2007. Replace the previous
# line plot with a scatter plot and place the x-axis on a
# logarithmic scale to better visualize the wide range of GDP
# values.
#
# 2. Topics Covered
# - Scatter plots with matplotlib (plt.scatter)
# - Applying logarithmic scaling to axes (plt.xscale)
# - Basic data visualization for correlation exploration
# ============================================

# 3. Python Script

# Create a scatter plot: gdp_cap on the x-axis, life_exp on the y-axis
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale to better visualize differences
plt.xscale('log')

# Display the plot
plt.show()

# ============================================
# 4. Additional Notes
# - Scatter plots are ideal for detecting relationships or correlations
#   between two numeric variables.
# - Log scaling is especially helpful when a variable spans multiple orders
#   of magnitude (like GDP per capita).
# - You can label axes later for clarity:
#     plt.xlabel("GDP per Capita (log scale)")
#     plt.ylabel("Life Expectancy")
# ============================================
