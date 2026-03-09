# ============================================
# 1. Task Description
# Explore whether the year a couple got married is related to the number
# of children they had at the time of divorce. Create a new column
# representing the marriage year and plot the average number of children
# by marriage year using a line plot.
#
# 2. Topics Covered
# - Extracting components from datetime columns (.dt.year)
# - Creating new time‑based features
# - Plotting trends over time with seaborn.lineplot()
# ============================================

# 3. Python Script

# Define the marriage_year column
divorce["marriage_year"] = divorce["marriage_date"].dt.year

# Create a line plot showing the average number of kids by year
sns.lineplot(x="marriage_year", y="num_kids", data=divorce)
plt.show()

# ============================================
# 4. Additional Notes
# Visualizing relationships over time
# - Extracting .dt.year allows analysis of trends at a year-granular level.
# - lineplot() automatically computes mean num_kids for each marriage year.
# - Time‑based visualizations help reveal patterns such as:
#       • Families getting smaller or larger over decades
#       • Social or economic trends affecting family size
#
# Context:
# pandas as pd
