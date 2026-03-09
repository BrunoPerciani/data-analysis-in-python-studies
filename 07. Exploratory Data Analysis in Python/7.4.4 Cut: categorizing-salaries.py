# ============================================
# 1. Task Description
# Categorize salary values into levels based on quartile cut points.
# Use pd.cut() to map Salary_USD into four groups:
#   - entry    (below 25th percentile)
#   - mid      (25th to median)
#   - senior   (median to 75th percentile)
#   - exec     (above 75th percentile)
# Then visualize the distribution of salary levels across different
# company sizes using a count plot.
#
# 2. Topics Covered
# - Creating category labels
# - Defining bin edges using summary statistics
# - Categorizing numeric values with pd.cut()
# - Plotting grouped categorical distributions
# ============================================

# 3. Python Script

# Create salary labels
salary_labels = ["entry", "mid", "senior", "exec"]

# Create the salary ranges list
salary_ranges = [
    0,
    twenty_fifth,
    salaries_median,
    seventy_fifth,
    salaries["Salary_USD"].max()
]

# Create salary_level
salaries["salary_level"] = pd.cut(
    salaries["Salary_USD"],
    bins=salary_ranges,
    labels=salary_labels
)

# Plot the count of salary levels at companies of different sizes
sns.countplot(data=salaries, x="Company_Size", hue="salary_level")
plt.show()

# ============================================
# 4. Additional Notes
# Categorizing salaries
# - pd.cut() assigns each Salary_USD into one of the bins defined by
#   salary_ranges. Each bin is mapped to a corresponding label.
# - Using quartiles (20th, median, 75th percentile) ensures balanced and
#   interpretable ranges aligned with the distribution of salaries.
# - This new feature (salary_level) is useful for:
#       • visualizing salary segmentation
#       • detecting patterns across company sizes
#       • modeling and feature engineering
#
# Interpretation:
# - The resulting count plot shows how salary tiers vary by company size.
# - Larger companies may have more senior/exec-level salaries, while
#   smaller companies may lean toward entry/mid salary levels.
#
# Context:
# pandas (pd), matplotlib.pyplot (plt), and seaborn (sns) are imported.
# The DataFrame `salaries` contains Salary_USD and Company_Size.
# The variables twenty_fifth, salaries_median, and seventy_fifth were
# computed previously.
# ============================================
