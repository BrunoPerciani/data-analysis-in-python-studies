# ============================================
# 1. Task Description
# Create a box plot to examine the distribution of final grades (G3)
# across different study time categories. This allows comparison of
# medians, quartiles, and variability among students who study different
# amounts each week.
#
# 2. Topics Covered
# - Creating box plots with seaborn.catplot()
# - Controlling category ordering for meaningful comparisons
# - Visual interpretation of distributions across subgroups
# ============================================

# 3. Python Script

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(
    x="study_time",
    y="G3",
    data=student_data,
    kind="box",
    order=study_time_order
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Create and interpret a box plot
# - Box plots show the median, interquartile range (IQR),
#   and potential outliers of the numeric variable (G3).
# - Ordering study_time logically ensures a meaningful comparison.
# - Compared to bar plots (which only show means), box plots reveal:
#       • grade variability within each study group  
#       • skewness  
#       • whether higher study times shift the entire distribution upward  
#
# Interpretation:
# - If the median and overall box rise with higher study_time categories,
#   this suggests that more studying is associated with better grades.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `student_data` contains 'study_time' and 'G3'.
# ============================================
