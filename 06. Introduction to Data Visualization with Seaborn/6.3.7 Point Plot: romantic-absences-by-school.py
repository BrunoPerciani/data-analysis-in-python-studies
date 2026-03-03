# ============================================
# 1. Task Description
# Create a point plot to compare the number of school absences between
# students who are in a romantic relationship and those who are not.
# Add subgroups based on the school each student attends, and use the
# median instead of the mean to summarize absences. Remove confidence
# intervals for a cleaner visualization.
#
# 2. Topics Covered
# - Point plots with seaborn.catplot()
# - Using estimator=median to summarize distributions
# - Adding subgroups with hue
# - Removing confidence intervals with errorbar=None
# ============================================

# 3. Python Script

# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(
    x="romantic",
    y="absences",
    data=student_data,
    kind="point",
    hue="school",
    errorbar=None,
    estimator=median
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Point plots with subgroups
# - Point plots normally plot the mean of the y‑variable per category.
#   Using estimator=median makes the plot more robust to extreme absences.
# - hue="school" creates subgroup comparisons within each romantic
#   category (yes/no relationship).
# - Removing error bars (errorbar=None) keeps the plot visually simple.
#
# Interpretation:
# - This visualization helps answer:
#       “Do students in romantic relationships miss more or fewer classes,
#        and does this differ by school?”
# - Differences in point height across romance categories and schools
#   highlight attendance behavioral patterns.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `student_data` contains 'romantic', 'absences', and 'school'.
# ============================================
