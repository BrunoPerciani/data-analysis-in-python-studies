# ============================================
# 1. Task Description
# Create a box plot to visualize the distribution of ages for male and
# female respondents in a youth survey dataset. Customize the appearance
# of the plot by applying a "darkgrid" style and a manually defined
# two‑color palette.
#
# 2. Topics Covered
# - Customizing Seaborn styles with sns.set_style()
# - Applying a custom color palette with sns.set_palette()
# - Creating box plots using seaborn.catplot()
# ============================================

# 3. Python Script

# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set a custom color palette
sns.set_palette(["#39A7D0", "#36ADA4"])

# Create the box plot of age distribution by gender
sns.catplot(
    x="Gender",
    y="Age",
    data=survey_data,
    kind="box"
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Using a custom palette
# - sns.set_style("darkgrid") adds a dark grid background that enhances
#   readability of box plots and other numeric comparisons.
# - sns.set_palette([...]) applies a list of custom colors. Here, two
#   hex colors are used to differentiate gender categories.
# - Box plots show median, quartiles, and potential outliers, making them
#   ideal for summarizing age distributions between male and female
#   respondents.
#
# Interpretation:
# - Differences in medians or spread between genders can reveal age
#   composition of the survey sample.
# - This forms part of a basic demographic summary, which is an important
#   first step in understanding any new dataset.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `survey_data` contains 'Gender' and 'Age'.
# ============================================
