# ============================================
# 1. Task Description
# Create a box plot to compare the distribution of final grades (G3)
# between students who have Internet access at home and those who do not.
# Add subgrouping by location (Urban vs. Rural) and remove outliers from
# the visualization to focus on the core distribution.
#
# 2. Topics Covered
# - Creating box plots with seaborn.catplot()
# - Using hue to create subgroups inside categorical plots
# - Omitting outliers using showfliers=False
# ============================================

# 3. Python Script

# Create a box plot with subgroups and omit the outliers
sns.catplot(
    x="internet",
    y="G3",
    data=student_data,
    kind="box",
    hue="location",
    showfliers=False
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Omitting outliers
# - Outliers can stretch the y‑axis and make it harder to compare the
#   central parts of the distribution.
# - Setting showfliers=False hides these extreme values so the interquartile
#   range and median are easier to interpret.
#
# Interpretation:
# - This plot helps answer whether having Internet access is associated
#   with higher final grades.
# - Subgrouping by location makes it possible to compare:
#       • Urban students with Internet  
#       • Urban students without Internet  
#       • Rural students with Internet  
#       • Rural students without Internet
# - Differences in median and IQR between groups reveal how access and
#   environment might affect performance.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `student_data` includes 'internet', 'G3', and 'location'.
# ============================================
