# ============================================
# 1. Task Description
# Create a point plot to examine whether the quality of a student's
# family relationship (famrel) is associated with the number of school
# absences. Remove the default line segments connecting the markers to
# emphasize individual category estimates.
#
# 2. Topics Covered
# - Point plots using seaborn.catplot()
# - Customizing the appearance of point plots
# - Removing connecting lines with linestyle='none'
# - Adding caps to confidence intervals (capsize)
# ============================================

# 3. Python Script

# Remove the lines joining the points
sns.catplot(
    x="famrel",
    y="absences",
    data=student_data,
    kind="point",
    capsize=0.2,
    linestyle='none'
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Customizing point plots
# - Point plots display summary statistics (typically means) for each
#   category along with confidence intervals.
# - Setting linestyle='none' removes the line that normally connects
#   points across categories, making each point stand out clearly.
# - capsize adds small horizontal ticks to the confidence intervals for
#   better visibility.
#
# Interpretation:
# - This visualization helps assess whether students with stronger family
#   relationships tend to have more or fewer absences.
# - If points decrease as famrel increases, it may indicate that students
#   with better family support miss school less frequently.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `student_data` contains 'famrel' and 'absences'.
# ============================================
