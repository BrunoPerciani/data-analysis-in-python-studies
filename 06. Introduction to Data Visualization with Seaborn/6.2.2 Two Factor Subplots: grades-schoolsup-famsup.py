# ============================================
# 1. Task Description
# Create a two-factor faceted scatterplot showing the relationship 
# between first‑semester grade (G1) and final grade (G3), with subplots
# based on whether the student received extra educational support from
# their school (schoolsup) and/or family (famsup). This allows visual
# comparison of how support interventions relate to academic outcomes.
#
# 2. Topics Covered
# - Creating multi‑factor faceted subplots using seaborn.relplot()
# - Controlling subplot order with col_order and row_order
# - Visual comparison across categorical combinations
# ============================================

# 3. Python Script

# Adjust further to add subplots based on family support
sns.relplot(
    x="G1",
    y="G3",
    data=student_data,
    kind="scatter",
    col="schoolsup",
    col_order=["yes", "no"],
    row="famsup",
    row_order=["yes", "no"]
)

# Show plot
plt.show()

# ============================================
# 4. Additional Notes
# Creating two-factor subplots
# - relplot() allows facetting by both row and column categories.
# - Using row="famsup" and col="schoolsup" creates a grid of 4 scatterplots
#   representing combinations of:
#       (School Support: yes/no) × (Family Support: yes/no)
# - This makes it easy to visually inspect whether the G1→G3 relationship
#   changes depending on educational support context.
#
# Interpretation:
# - A strong positive trend across all subplots suggests that G1 is a good
#   predictor of G3 regardless of support type.
# - Differences in slope or scatter between subsets may reveal differences
#   in how support affects grade improvement.
#
# Context:
# seaborn (sns) and matplotlib.pyplot (plt) are imported.
# The DataFrame `student_data` contains 'G1', 'G3', 'schoolsup', and 'famsup'.
# ============================================
