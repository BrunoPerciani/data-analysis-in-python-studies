# ============================================
# 1. Task Description
# Create a scatter plot showing the relationship between student absences
# and final course grade (G3), while segmenting students by their living
# location (Rural vs. Urban). The goal is to visualize how absences may
# affect student performance across subgroups.
#
# 2. Topics Covered
# - Scatterplots with seaborn
# - Using hue to create subgroup distinctions
# - Controlling legend order with hue_order
# ============================================

# 3. Python Script

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change the legend order in the scatter plot
sns.scatterplot(
    x="absences",
    y="G3",
    data=student_data,
    hue="location",
    hue_order=["Rural", "Urban"]
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Hue and scatter plots
# - Using the hue parameter allows you to visualize subgroups within the
#   data. Here, we separate students by whether they live in a Rural or
#   Urban location.
# - hue_order ensures that the legend appears in a specific order rather
#   than alphabetical.
# - Scatterplots are a great first step in identifying trends or
#   potential correlations (e.g., more absences could be associated with
#   lower final grades).
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `student_data` contains 'absences', 'G3', and 'location'.
# ============================================
