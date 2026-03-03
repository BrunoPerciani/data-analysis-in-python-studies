# ============================================
# 1. Task Description
# Create a box plot to compare the distribution of final grades (G3)
# between students who are in a romantic relationship and those who are
# not. Modify the whiskers so they extend to the minimum and maximum
# values in each group.
#
# 2. Topics Covered
# - Box plots with seaborn.catplot()
# - Customizing whiskers using the whis parameter
# - Comparing distributions across binary categories
# ============================================

# 3. Python Script

# Set the whiskers at the min and max values
sns.catplot(
    x="romantic",
    y="G3",
    data=student_data,
    kind="box",
    whis=[0, 100]
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Adjusting the whiskers
# - The whis parameter determines how far the whiskers extend:
#       • whis=[0, 100] sets the whiskers at the actual minimum and
#         maximum values of the data (full range).
# - Default whiskers typically extend to 1.5 × IQR, marking potential
#   outliers beyond that range.
# - Extending whiskers to min/max removes the emphasis on outliers and
#   shows the complete range of values in each category.
#
# Interpretation:
# - This visualization helps determine whether being in a romantic
#   relationship is associated with different final‑grade distributions.
# - Full‑range whiskers allow easy comparison of extreme values but may
#   obscure traditional outlier detection.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `student_data` contains 'romantic' and 'G3'.
# ============================================
