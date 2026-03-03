# ============================================
# 1. Task Description
# Create a line plot to explore how the fuel efficiency of cars
# (measured in miles per gallon, mpg) has changed over time, using the
# model_year variable from the seaborn mpg dataset.
#
# 2. Topics Covered
# - Line plots with seaborn.relplot()
# - Visualizing trends over time
# - Interpreting aggregated patterns in continuous variables
# ============================================

# 3. Python Script

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(
    x='model_year',
    y='mpg',
    data=mpg,
    kind='line'
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Interpreting line plots
# - Line plots display changes in a variable across an ordered dimension.
#   Here, model_year acts as a timeline, allowing us to see fuel-efficiency
#   trends across car model years.
# - Typically, mpg increases over time in this dataset due to improvements
#   in automotive engineering, emissions standards, and energy constraints.
# - relplot(kind='line') automatically computes mean values for each year
#   when duplicate x-values exist, making it ideal for aggregated trends.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `mpg` contains 'model_year' and 'mpg'.
# ============================================
