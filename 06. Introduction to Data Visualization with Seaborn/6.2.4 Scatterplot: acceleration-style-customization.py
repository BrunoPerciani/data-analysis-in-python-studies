# ============================================
# 1. Task Description
# Create a scatter plot showing the relationship between a car’s
# acceleration (time to reach 60 mph) and its fuel efficiency (mpg),
# while differentiating cars by their country of origin using both
# color (hue) and marker style (style).
#
# 2. Topics Covered
# - Using seaborn.relplot() for scatter visualization
# - Mapping categorical variables to both hue and style
# - Exploring multivariate relationships in automotive datasets
# ============================================

# 3. Python Script

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(
    x="acceleration",
    y="mpg",
    data=mpg,
    kind="scatter",
    hue="origin",
    style="origin"
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Changing the style of scatter plot points
# - Mapping 'origin' to both hue and style allows clear differentiation
#   between regions (e.g., USA, Europe, Asia).
# - Acceleration is measured as time to go from 0 → 60 mph:
#       • higher values = slower acceleration
#       • lower values = quicker acceleration
#
# Interpretation:
# - By plotting mpg against acceleration, you can visually inspect whether
#   more efficient cars (higher mpg) also tend to accelerate faster or slower.
# - Using both color and marker shape ensures better readability,
#   especially in dense clusters of points.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `mpg` includes 'acceleration', 'mpg', and 'origin'.
# ============================================
