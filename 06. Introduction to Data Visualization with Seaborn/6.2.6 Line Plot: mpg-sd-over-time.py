# ============================================
# 1. Task Description
# Use a line plot to visualize how the distribution of miles per gallon
# (mpg) has changed over time. Instead of showing only the mean mpg per
# model year, display standard deviation shading to highlight variability
# in fuel efficiency over different years.
#
# 2. Topics Covered
# - Line plots with seaborn.relplot()
# - Visualizing variability using standard deviation shading
# - Understanding changes in both central tendency and spread over time
# ============================================

# 3. Python Script

# Make the shaded area show the standard deviation
sns.relplot(
    x="model_year",
    y="mpg",
    data=mpg,
    kind="line",
    errorbar="sd"
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Visualizing standard deviation with line plots
# - Using errorbar="sd" tells seaborn to compute the standard deviation
#   of mpg for each model year and display it as a shaded band around the
#   mean line.
# - This lets us examine not just the trend in average mpg over time, but
#   also how spread/variability in mpg changes across years.
#
# Interpretation:
# - If the shaded area narrows over time, mpg values became more consistent.
# - If the shaded area widens, cars varied more in mpg during that period.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `mpg` contains 'model_year' and 'mpg'.
# ============================================
