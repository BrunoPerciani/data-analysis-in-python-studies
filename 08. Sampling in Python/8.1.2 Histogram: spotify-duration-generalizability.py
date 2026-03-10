# ============================================
# 1. Task Description
# Visualize the population‑level distribution of song durations in minutes
# using a histogram. This will be used to compare the duration_minutes
# distribution from a second sample and assess whether the sample appears
# representative of the population.
#
# 2. Topics Covered
# - Histogram visualization with pandas/matplotlib
# - Understanding distribution shape
# - Comparing sample distributions to population distributions
# ============================================

# 3. Python Script

# Visualize the distribution of duration_minutes as a histogram
spotify_population["duration_minutes"].hist(
    bins=np.arange(0, 15.5, 0.5)
)
plt.show()

# ============================================
# 4. Additional Notes
# Are these findings generalizable?
# - Histograms help visualize the distribution of a numeric variable,
#   revealing pattern, shape, skew, and potential outliers.
# - The spotify_population histogram serves as the “true” population
#   distribution of song durations.
# - You can compare this plot to the distribution of
#   spotify_mysterious_sample2['duration_minutes']:
#       If the shapes look similar (e.g., similar peaks, skew, spread),
#       then the sample may be representative.
# - Large deviations in shape between the sample and population
#   distribution suggest sampling bias or insufficient sample size.
#
# Context:
# pandas is loaded as pd,
# numpy as np,
# matplotlib.pyplot as plt,
# and the DataFrame `spotify_population` contains 'duration_minutes'.
# ============================================
