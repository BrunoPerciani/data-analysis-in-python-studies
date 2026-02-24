# ============================================
# 1. Task Description
# Create overlaid histograms to compare the price distributions of
# conventional and organic avocados. The goal is to visualize differences
# in average prices between the two avocado types.
#
# 2. Topics Covered
# - Subsetting data for plotting
# - Creating histograms with .hist()
# - Adjusting the number of bins
# - Overlaying multiple plots with transparency (alpha)
# - Adding a legend to distinguish categories
# ============================================

# 3. Python Script

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(bins=20, alpha=0.5)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(bins=20, alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

# ============================================
# 4. Additional Notes
# Price of conventional vs. organic avocados
# Creating multiple histograms for different subsets of data is a simple
# way to compare distributions. Overlaying them helps reveal differences
# in variability and typical price ranges.
#
# Tips:
# - Use alpha to control transparency when overlaying histograms.
# - Ensure both subsets use the same bin size for fair comparison.
#
# Context:
# matplotlib.pyplot has been imported as plt.
# pandas has been imported as pd.
# The DataFrame `avocados` contains avocado price and type data.
# ============================================
