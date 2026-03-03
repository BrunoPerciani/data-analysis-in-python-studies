# ============================================
# 1. Task Description
# Visualize how many students attend each school (GP or MS), while also
# segmenting counts by student location (Rural vs. Urban). This allows
# comparison of subgroup distributions across the two schools.
#
# 2. Topics Covered
# - Categorical count plots with seaborn
# - Using hue to create subgroup comparisons
# - Custom color palettes using dictionaries
# ============================================

# 3. Python Script

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(
    x="school",
    data=student_data,
    hue="location",
    palette=palette_colors
)

# Display plot
plt.show()

# ============================================
# 4. Additional Notes
# Hue and count plots
# - Count plots show the number of observations in each category.
# - The hue argument adds subgroup separation within each category so
#   you can compare, for example, how many Rural vs. Urban students attend
#   each school.
# - Customizing the palette allows explicit control over the color mapping.
#
# Interpretation:
# - Differences in the heights of Rural and Urban bars within each school
#   reveal demographic patterns.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `student_data` contains columns 'school' and 'location'.
# ============================================
