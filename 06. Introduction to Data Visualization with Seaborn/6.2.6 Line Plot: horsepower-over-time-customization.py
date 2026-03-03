# ============================================
# 1. Task Description
# Visualize how the average horsepower of cars has changed over time,
# while comparing trends across countries of origin (USA, Europe, Japan).
# Add markers to the line plot and ensure each subgroup uses consistent
# line styling to clearly distinguish trends.
#
# 2. Topics Covered
# - Line plots using seaborn.relplot()
# - Visualizing subgroup trends with hue and style
# - Adding markers and removing dashed line styles
# ============================================

# 3. Python Script

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(
    x="model_year",
    y="horsepower",
    data=mpg,
    kind="line",
    errorbar=None,
    style="origin",
    hue="origin",
    markers=True,
    dashes=False
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Plotting subgroups in line plots
# - Using hue="origin" colors the lines by car origin.
# - Using style="origin" and markers=True gives each origin a distinct
#   marker shape, improving readability.
# - Setting dashes=False ensures all lines are solid, making marker
#   differences more noticeable.
#
# Interpretation:
# - This visualization helps answer whether horsepower increased,
#   decreased, or stayed stable over time.
# - It also shows whether trends differ among American, European, and
#   Japanese cars.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `mpg` contains 'model_year', 'horsepower', and 'origin'.
# ============================================
