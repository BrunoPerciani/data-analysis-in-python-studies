# ============================================
# 1. Task Description
# Create a basic line plot using matplotlib to visualize the evolution
# of world population from 1950 to 2100. The `year` list contains the
# years, and the `pop` list contains the corresponding population
# estimates. The goal is to display how population changes over time.
#
# 2. Topics Covered
# - Accessing list elements (indexing / negative indexing)
# - Basic matplotlib usage: plt.plot(), plt.show()
# - Line plot construction: x‑axis (year), y‑axis (population)
# ============================================

# 3. Python Script

# Print the last values of the year and population lists
print(year[-1])   # last year value
print(pop[-1])    # last population value

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Create a line plot with year on the x-axis and population on the y-axis
plt.plot(year, pop)

# Display the plot
plt.show()

# ============================================
# 4. Additional Notes
# - Negative indexing is useful when you need the last element of a list.
# - plt.plot(year, pop) automatically connects points in order, forming a line.
# - For more readable axes, you could later add labels:
#     plt.xlabel("Year")
#     plt.ylabel("Population")
# ============================================
