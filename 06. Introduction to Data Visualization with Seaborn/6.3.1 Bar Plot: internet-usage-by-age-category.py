# ============================================
# 1. Task Description
# Create a count plot to visualize how often young people report using
# the Internet each day. Then separate the visualization into multiple
# subplots based on age category to compare usage patterns across age
# groups.
#
# 2. Topics Covered
# - Categorical count plots using seaborn.catplot()
# - Faceting subplots using the 'col' parameter
# - Visual comparison of distributions across subgroups
# ============================================

# 3. Python Script

# Separate into column subplots based on age category
sns.catplot(
    y="Internet usage",
    data=survey_data,
    kind="count",
    col="Age Category"
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Count plots
# - A count plot displays how many observations fall into each category.
# - Using col="Age Category" creates a separate subplot for each age
#   group, making it easy to compare how reported Internet usage varies
#   by age.
# - Swapping x and y (here we use y="Internet usage") helps readability
#   when labels are long or categories are numerous.
#
# Interpretation:
# - This plot helps answer whether Internet usage patterns differ across
#   younger vs. older survey respondents.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `survey_data` contains 'Internet usage' and 'Age Category'.
# ============================================
