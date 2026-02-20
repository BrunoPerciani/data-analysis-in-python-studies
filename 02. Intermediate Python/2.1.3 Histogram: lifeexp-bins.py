# ============================================
# 1. Task Description
# Build two histograms of the life expectancy data (life_exp) by
# varying the number of bins. The goal is to visualize how bin
# size affects the shape and interpretability of a histogram.
# A histogram with too few bins oversimplifies the data, while a
# histogram with too many bins introduces unnecessary noise.
#
# 2. Topics Covered
# - plt.hist() for histogram creation
# - Controlling bin size with the 'bins' parameter
# - plt.show() to display figures
# - plt.clf() to clear the figure for a new plot
# ============================================

# 3. Python Script

# Build histogram with 5 bins
plt.hist(life_exp, bins=5)

# Show plot and clear the figure
plt.show()
plt.clf()

# Build histogram with 20 bins for more granularity
plt.hist(life_exp, bins=20)

# Show plot and clear the figure again
plt.show()
plt.clf()

# ============================================
# 4. Additional Notes
# - plt.clf() (clear figure) ensures the next plot starts fresh.
# - Increasing bins reveals more details but can also introduce clutter.
# - Later, you can add axis labels:
#     plt.xlabel("Life Expectancy")
#     plt.ylabel("Frequency")
# ============================================
