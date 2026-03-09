# ============================================
# 1. Task Description
# Add descriptive statistics to the planes DataFrame by computing the
# mean ticket price for each destination. Use .groupby() with .transform()
# so that the resulting values are aligned with the original DataFrame
# shape and stored in a new column.
#
# 2. Topics Covered
# - Using groupby().transform() for row-aligned summary statistics
# - Applying custom functions with lambda
# - Adding descriptive columns for downstream analysis
# ============================================

# 3. Python Script

# Mean Price by Destination
planes["price_destination_mean"] = planes.groupby("Destination")["Price"].transform(
    lambda x: x.mean()
)

print(planes[["Destination", "price_destination_mean"]].value_counts())

# ============================================
# 4. Additional Notes
# Adding descriptive statistics
# - groupby().transform() returns a series with the same length as the
#   original DataFrame, making it ideal for adding per-group summary
#   statistics as new columns.
# - transform(mean) gives every row in a group the same value: the mean
#   price for that destination.
# - This is different from groupby().agg(), which reduces rows.
#
# Why this is useful:
# - Enables comparisons such as:
#       Price − Mean Price (Destination)
# - Facilitates feature engineering for modeling or further analysis.
# - Supports ranking, filtering, and visualizations by group-level stats.
#
# Context:
# pandas is imported as pd, numpy as np, and seaborn as sns.
# The DataFrame `planes` includes 'Destination' and 'Price'.
# ============================================
