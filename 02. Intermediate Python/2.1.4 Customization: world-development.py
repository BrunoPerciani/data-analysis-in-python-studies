# ============================================
# 1. Task Description
# Create a scatter plot of GDP per capita vs. life expectancy for
# countries in 2007. Customize the visualization by:
#   • varying point size based on population,
#   • applying color coding,
#   • using logarithmic scaling for GDP,
#   • adding axis labels, title, custom tick labels,
#   • annotating specific countries (India, China),
#   • enabling grid lines for readability.
#
# This exercise demonstrates combining several matplotlib
# customization techniques to enhance data storytelling.
#
# 2. Topics Covered
# - Scatter plots with matplotlib (plt.scatter)
# - Marker size scaling and color arrays
# - Axis transformations (log scale)
# - Text annotations with plt.text()
# - Gridlines with plt.grid(True)
# ============================================

# 3. Python Script

# Create scatter plot:
#   x-axis → GDP per capita
#   y-axis → life expectancy
#   s → point size scaled by population
#   c → colors assigned to each country
plt.scatter(
    x=gdp_cap,
    y=life_exp,
    s=np.array(pop) * 2,   # scale populations for marker size
    c=col,                 # color list
    alpha=0.8              # transparency
)

# Apply log scale to x-axis because GDP per capita spans orders of magnitude
plt.xscale('log')

# Add axis labels
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')

# Add a title
plt.title('World Development in 2007')

# Replace x-tick labels for readability
plt.xticks(
    [1000, 10000, 100000],
    ['1k', '10k', '100k']
)

# Additional customizations:
# Add text annotations for specific countries
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add gridlines to improve readability of the scatter plot
plt.grid(True)

# Display the plot
plt.show()

# ============================================
# 4. Additional Notes
# - Using plt.text(x, y, text) lets you annotate specific points.
# - Gridlines help visually align points across axes.
# - If the labels overlap points, consider adding:
#       fontsize=10, weight='bold'
#       or using plt.annotate() for more precise control.
# ============================================
