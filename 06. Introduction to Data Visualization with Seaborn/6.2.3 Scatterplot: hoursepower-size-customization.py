# ============================================
# 1. Task Description
# Create a scatter plot showing the relationship between car horsepower
# and fuel efficiency (mpg), while varying both color and point size by
# the number of cylinders. This allows visual comparison of how engine
# characteristics relate to fuel consumption across different engine types.
#
# 2. Topics Covered
# - Figure-level scatter plots using seaborn.relplot()
# - Encoding a numeric categorical variable using hue and size
# - Visualizing multi-dimensional relationships
# ============================================

# 3. Python Script

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(
    x="horsepower",
    y="mpg",
    data=mpg,
    kind="scatter",
    size="cylinders",
    hue="cylinders"
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Changing the size of scatter plot points
# - relplot() allows mapping additional variables, such as cylinders,
#   to point size and color, making the visualization multidimensional.
# - Cars with more cylinders typically have:
#       • higher horsepower
#       • lower mpg
# - Using both hue and size helps emphasize this pattern clearly.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `mpg` includes 'horsepower', 'mpg', and 'cylinders'.
# ============================================
