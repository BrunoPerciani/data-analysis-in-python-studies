# ============================================
# 1. Task Description
# Transform skewed GDP per capita values using a natural logarithm to
# linearize the relationship with happiness scores. Visualize the 
# transformed relationship with a scatterplot and compute the correlation
# between log-transformed GDP per capita and happiness score.
#
# 2. Topics Covered
# - Log transformation using numpy
# - Scatterplots with seaborn
# - Exploring linearity after transformation
# - Computing correlation with pandas .corr()
# ============================================

# 3. Python Script

# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of happiness_score vs. log_gdp_per_cap
sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)

# ============================================
# 4. Additional Notes
# Transforming variables
# - When a predictor variable (e.g., GDP per capita) is highly skewed, 
#   applying a transformation—commonly the natural logarithm—can help 
#   linearize its relationship with the response variable.
# - A more linear relationship improves interpretability and allows 
#   correlation measures (such as Pearson correlation) to better reflect 
#   the true association.
#
# Interpretation:
# - If the correlation increases after log-transforming GDP per capita, 
#   this implies that the log scale captures the economic impact on 
#   happiness more realistically.
#
# Context:
# pandas as pd, numpy as np, seaborn as sns, and matplotlib.pyplot as plt 
# are already imported. The DataFrame `world_happiness` includes 
# 'gdp_per_cap' and 'happiness_score'.
# ============================================
