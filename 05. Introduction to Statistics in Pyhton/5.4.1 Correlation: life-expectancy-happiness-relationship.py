# ============================================
# 1. Task Description
# Visualize and quantify the relationship between life expectancy and
# happiness score across countries using the 2019 World Happiness Report
# dataset. Create a scatterplot with a trendline and compute the Pearson
# correlation between the two variables.
#
# 2. Topics Covered
# - Visualizing relationships with seaborn.lmplot()
# - Linear trendline visualization
# - Computing correlations with pandas .corr()
# - Combining visual and numeric insights
# ============================================

# 3. Python Script

# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x='life_exp', y='happiness_score', data=world_happiness, ci=None)

# Show plot
plt.show()

# Correlation between life_exp and happiness_score
cor = world_happiness['happiness_score'].corr(world_happiness['life_exp'])
print(cor)

# ============================================
# 4. Additional Notes
# Relationships between variables
# - lmplot() provides a scatterplot with an optional linear regression line.
# - If the trendline slopes upward, it suggests higher life expectancy
#   tends to be associated with higher happiness scores.
# - The correlation coefficient quantifies this: values close to +1
#   indicate a strong positive linear relationship.
#
# Context:
# seaborn as sns, matplotlib.pyplot as plt, and pandas as pd are loaded.
# The DataFrame `world_happiness` contains columns including 'life_exp'
# and 'happiness_score'.
# ============================================
