# ============================================
# 1. Task Description
# Visually and statistically inspect the "Price" and "Duration" variables
# in the planes DataFrame to identify potential outliers. Use a histogram
# to visualize the distribution of flight prices and .describe() to
# examine summary statistics for flight duration.
#
# 2. Topics Covered
# - Histograms for visualizing skew and extreme values
# - Descriptive statistics (.describe()) for detecting spread and outliers
# - Combining numeric + visual methods to confirm irregular values
# ============================================

# 3. Python Script

# Plot a histogram of flight prices
sns.histplot(data=planes, x="Price")
plt.show()

# Display descriptive statistics for flight duration
print(planes["Duration"].describe())

# ============================================
# 4. Additional Notes
# Identifying outliers
# - Histograms help detect outliers visually: extreme values appear as
#   isolated bars far from the main cluster of the distribution.
# - If the "Price" histogram shows a long right tail or isolated high bars,
#   those values may be outliers worth investigating.
# - .describe() is useful for spotting outliers in numeric variables:
#       • Large differences between mean and median suggest skew.
#       • Extremely high max or extremely low min values relative to the
#         IQR can indicate outliers.
#
# Example considerations:
# - Price distributions often show high-end outliers due to premium tickets.
# - Duration distributions may show unusually long flights (e.g., > 20h)
#   which could be anomalies depending on the dataset.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `planes` contains numeric columns "Price" and "Duration".
# ============================================
