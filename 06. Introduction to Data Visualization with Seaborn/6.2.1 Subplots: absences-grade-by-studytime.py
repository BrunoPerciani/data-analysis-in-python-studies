# ============================================
# 1. Task Description
# Create multiple scatterplots showing the relationship between student
# absences and final grades, with separate subplots for each level of
# weekly study time. These facet plots allow you to visually compare
# whether the absences–performance relationship holds across study-time
# groups.
#
# 2. Topics Covered
# - Faceted scatterplots using seaborn.relplot()
# - Arranging subplots by row instead of column
# - Visual subgroup comparison
# ============================================

# 3. Python Script

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(
    x="absences",
    y="G3",
    data=student_data,
    kind="scatter",
    row="study_time"
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Creating subplots with col and row
# - relplot() is a figure-level function that can automatically create
#   subplots using row= or col= to facet data by category.
# - Using row="study_time" arranges the subplots vertically, making it
#   easier to compare slope and spread across study-time categories.
# - This visualization helps answer:
#       “Does the negative relationship between absences and final grade
#        persist across all levels of study time?”
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `student_data` contains 'absences', 'G3', and 'study_time'.
# ============================================
