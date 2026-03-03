# ============================================
# 1. Task Description
# Create a point plot displaying average acceleration for cars from each
# place of origin (USA, Europe, Japan). Rotate the x‑tick labels for
# improved readability.
#
# 2. Topics Covered
# - Point plots using seaborn.catplot()
# - Customizing plot appearance
# - Rotating x‑tick labels with Matplotlib’s plt.xticks()
# ============================================

# 3. Python Script

# Create point plot
sns.catplot(
    x="origin",
    y="acceleration",
    data=mpg,
    kind="point",
    linestyle="none",
    capsize=0.1
)

# Rotate x-tick labels
plt.xticks(rotation=90)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Rotating x-tick labels
# - plt.xticks(rotation=90) is a standalone Matplotlib function that
#   rotates x‑axis category labels for better visibility, especially when
#   labels are long or numerous.
# - In point plots, linestyle="none" removes connecting lines, and
#   capsize adds small horizontal markers to the confidence intervals.
#
# Interpretation:
# - Higher acceleration values represent slower acceleration.
# - Comparing across origins can reveal whether certain regions tend to
#   produce faster or slower‑accelerating cars.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `mpg` contains 'origin' and 'acceleration'.
# ============================================
