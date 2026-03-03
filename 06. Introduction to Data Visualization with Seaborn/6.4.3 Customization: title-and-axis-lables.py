# ============================================
# 1. Task Description
# Create a line plot to visualize how the average miles per gallon (mpg)
# has changed over time for cars from different places of origin. Improve
# readability by adding a descriptive title and customized axis labels.
#
# 2. Topics Covered
# - Line plots with seaborn.lineplot()
# - Adding titles and axis labels to Matplotlib Axes objects
# - Customizing plot readability for time‑trend visualizations
# ============================================

# 3. Python Script

# Create line plot
g = sns.lineplot(
    x="model_year",
    y="mpg_mean",
    data=mpg_mean,
    hue="origin"
)

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel="Car Model Year", ylabel="Average MPG")

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Adding a title and axis labels
# - seaborn.lineplot() returns a standard Matplotlib Axes object, so
#   titles and labels must be added using .set_title() and .set().
# - Titles help the viewer understand the purpose of the visualization.
# - Custom axis labels make the data more interpretable, especially when
#   abbreviations (e.g., “mpg”) may not be obvious to all audiences.
#
# Interpretation:
# - This plot reveals how fuel efficiency trends differ among cars from
#   different regions (e.g., USA, Europe, Japan) across model years.
# - Rising lines often indicate improved efficiency over time.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `mpg_mean` contains columns: 'model_year', 'mpg_mean',
# and 'origin'.
# ============================================
