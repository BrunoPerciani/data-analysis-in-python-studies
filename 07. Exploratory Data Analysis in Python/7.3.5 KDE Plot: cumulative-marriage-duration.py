# ============================================
# 1. Task Description
# Visualize cumulative kernel density estimates (KDEs) to explore the
# relationship between marriage duration and the number of children a
# couple had at the time of divorce. By using cumulative=True, KDE curves
# become cumulative distribution functions (CDFs), making it easier to
# compare how quickly each distribution accumulates probability mass.
#
# 2. Topics Covered
# - KDE plots with seaborn.kdeplot()
# - Visualizing cumulative distribution functions (CDFs)
# - Using hue to compare multiple distributions in one plot
# ============================================

# 3. Python Script

# Update the KDE plot to show a cumulative distribution function
sns.kdeplot(
    data=divorce,
    x="marriage_duration",
    hue="num_kids",
    cut=0,
    cumulative=True
)
plt.show()

# ============================================
# 4. Additional Notes
# Exploring with KDE plots
# - KDE plots estimate the probability density function of a continuous
#   variable. Setting cumulative=True converts the KDE into a smooth CDF.
# - Hue separates distributions by num_kids (1–5), allowing comparison:
#       • Steeper CDF → shorter typical marriage durations  
#       • Flatter CDF → longer durations  
# - Because divorce couples with 0 kids have missing num_kids values,
#   they are automatically excluded from the plot.
# - CDFs are helpful for answering questions such as:
#       “Which group tends to divorce earlier?”  
#       “How do distributions shift as family size increases?”
#
# Context:
# pandas as pd, seaborn as sns, and matplotlib.pyplot as plt are imported.
# The DataFrame `divorce` contains 'marriage_duration' and 'num_kids'.
# ============================================
