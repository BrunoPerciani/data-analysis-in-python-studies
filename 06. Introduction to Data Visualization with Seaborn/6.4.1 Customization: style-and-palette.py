# ============================================
# 1. Task Description
# Customize the style and color palette of a count plot visualizing how 
# often young people report listening to their parents’ advice. Use the 
# "RdBu" palette and the "whitegrid" style to improve readability.
#
# 2. Topics Covered
# - Modifying Seaborn styles with sns.set_style()
# - Changing color palettes with sns.set_palette()
# - Creating count plots with ordered categories
# ============================================

# 3. Python Script

# Change the color palette to "RdBu"
sns.set_style("whitegrid")
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes",
                  "Often", "Always"]

sns.catplot(
    x="Parents Advice",
    data=survey_data,
    kind="count",
    order=category_order
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Changing style and palette
# - sns.set_style("whitegrid") improves readability by adding a subtle 
#   background grid, especially useful for categorical plots.
# - sns.set_palette("RdBu") applies a diverging red‑to‑blue palette,
#   helping visually distinguish count differences across categories.
# - category_order controls the logical order of responses, ensuring the 
#   plot reflects the natural progression from low frequency to high.
#
# Interpretation:
# - The resulting plot reveals how frequently respondents report listening 
#   to their parents’ advice and whether certain categories dominate.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `survey_data` contains the column "Parents Advice".
# ============================================
