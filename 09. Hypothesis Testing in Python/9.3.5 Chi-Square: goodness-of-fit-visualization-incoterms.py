# ============================================
# 1. Task Description
# Visually compare observed vs. hypothesized distributions for the
# categorical variable 'vendor_inco_term' prior to a chi-square
# goodness-of-fit test. Plot observed counts in red and hypothesized
# counts in semi-transparent blue.
#
# 2. Topics Covered
# - Building hypothesized counts from proportions
# - Overlaying bar charts for observed vs. hypothesized frequencies
# - Visual checks before formal goodness-of-fit testing
# ============================================

# 3. Python Script

# Find the number of rows in late_shipments
n_total = len(late_shipments)

# Create n column that is prop column * n_total
hypothesized["n"] = hypothesized["prop"] * n_total

# Plot a red bar graph of n vs. vendor_inco_term for incoterm_counts
plt.bar(
    incoterm_counts["vendor_inco_term"],
    incoterm_counts["n"],
    color="red",
    label="Observed"
)

# Add a blue bar plot for the hypothesized counts
plt.bar(
    hypothesized["vendor_inco_term"],
    hypothesized["n"],
    alpha=0.5,
    color="blue",
    label="Hypothesized"
)

plt.legend()
plt.show()

# ============================================
# 4. Additional Notes
# Visualizing goodness of fit
# - Before running a chi-square goodness-of-fit test, plotting observed
#   vs. hypothesized counts helps spot clear discrepancies at a glance.
# - Ensure that:
#     • Categories are aligned (same order and labels in both DataFrames).
#     • Hypothesized proportions sum to 1.0 (CIP 0.05, DDP 0.10, EXW 0.75, FCA 0.10).
# - After this visual check, proceed with the formal chi-square test to
#   quantify the evidence against H0 (that observed data follow the
#   hypothesized distribution).
# ============================================
