# ============================================
# 1. Task Description
# Visualize the relationship between students’ weekly study time and their
# final grade (G3) using a customized bar plot. The study_time categories
# need to be ordered logically from lowest to highest, and confidence
# intervals should be disabled for a cleaner comparison.
#
# 2. Topics Covered
# - Custom ordering of categorical variables
# - Bar plots with seaborn.catplot()
# - Removing confidence intervals for cleaner visuals
# ============================================

# 3. Python Script

# List of categories from lowest to highest
category_order = [
    "<2 hours",
    "2 to 5 hours",
    "5 to 10 hours",
    ">10 hours"
]

# Turn off the confidence intervals
sns.catplot(
    x="study_time",
    y="G3",
    data=student_data,
    kind="bar",
    order=category_order,
    errorbar=None
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Customizing bar plots
# - When categorical variables have a natural progression, you should
#   explicitly set the order to ensure proper interpretation.
# - Bar plots show the *mean* of the numeric variable (G3) for each
#   category (study_time).
# - Setting errorbar=None removes confidence intervals, keeping the plot
#   simple and focused only on mean comparisons.
#
# Interpretation:
# - This plot helps determine whether students who report studying more
#   hours per week tend to achieve higher final grades.
# - Increasing bar heights across categories would suggest a positive
#   relationship between study time and performance.
#
# Context:
# seaborn as sns and matplotlib.pyplot as plt are imported.
# The DataFrame `student_data` contains 'study_time' and 'G3'.
# ============================================
