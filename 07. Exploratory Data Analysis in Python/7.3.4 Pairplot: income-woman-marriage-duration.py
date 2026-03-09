# ============================================
# 1. Task Description
# Use a pairplot to visualize the relationship between women’s income
# (income_woman) and the duration of marriage (marriage_duration).
# Pairplots display pairwise scatterplots and univariate distributions
# for the selected variables, allowing easy comparison.
#
# 2. Topics Covered
# - Visualizing variable relationships with seaborn.pairplot()
# - Exploring bivariate and univariate distributions
# - Using pairplot for quick exploratory data analysis (EDA)
# ============================================

# 3. Python Script

# Create a pairplot for income_woman and marriage_duration
sns.pairplot(data=divorce, vars=["income_woman", "marriage_duration"])
plt.show()

# ============================================
# 4. Additional Notes
# Visualizing multiple variable relationships
# - pairplot() generates:
#       • scatterplots for each pair of variables
#       • histograms or KDE plots on the diagonal
# - This is useful for detecting:
#       • linear or nonlinear relationships
#       • clustering or subgroups
#       • skewness and distribution shape
#       • potential outliers
#
# Interpretation:
# - You can quickly assess whether higher or lower income is associated
#   with longer or shorter marriage duration.
#
# Context:
# pandas is loaded as pd, matplotlib.pyplot as plt, and seaborn as sns.
# The DataFrame `divorce` contains numeric columns 'income_woman'
# and 'marriage_duration'.
# ============================================
