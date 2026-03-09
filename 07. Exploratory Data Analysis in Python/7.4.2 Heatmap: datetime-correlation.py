# ============================================
# 1. Task Description
# Extract datetime-based features from the "date_of_response" column in
# the salaries dataset and visualize correlations using a heatmap. The
# goal is to expand the dataset with meaningful temporal attributes and
# inspect how they relate to other numeric variables.
#
# 2. Topics Covered
# - Feature extraction from datetime columns using .dt accessor
# - Adding month and weekday variables for time-based analysis
# - Computing a correlation matrix with .corr()
# - Visualizing correlations using seaborn.heatmap()
# ============================================

# 3. Python Script

# Get the month of the response
salaries["month"] = salaries["date_of_response"].dt.month

# Extract the weekday of the response
salaries["weekday"] = salaries["date_of_response"].dt.weekday

# Create a heatmap
sns.heatmap(salaries.corr(numeric_only=True), annot=True)
plt.show()

# ============================================
# 4. Additional Notes
# Extracting features for correlation
# - The .dt accessor allows extracting components such as month, weekday,
#   year, hour, etc., from datetime64[ns] values.
# - Adding time-based features can reveal behavioral or seasonal trends
#   in salary responses.
# - salaries.corr(numeric_only=True) ensures only numeric columns are
#   included in the correlation matrix, avoiding errors.
# - Heatmaps make it easy to visually compare relationships between
#   variables and identify potentially strong or weak correlations.
#
# Interpretation:
# - If month or weekday show correlation with Salary_USD, this might hint
#   at seasonality or timing effects in responses.
# - Heatmaps highlight both positive and negative linear associations.
#
# Context:
# seaborn (sns), pandas (pd), and matplotlib.pyplot (plt) are imported.
# The DataFrame `salaries` includes a datetime column 'date_of_response'.
# ============================================
