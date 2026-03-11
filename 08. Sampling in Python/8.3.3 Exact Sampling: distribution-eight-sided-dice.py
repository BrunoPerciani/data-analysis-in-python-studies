# ============================================
# 1. Task Description
# Construct the exact sampling distribution of the mean roll from five
# eight‑sided dice. Enumerate ALL possible outcomes using expand_grid(),
# compute the mean of each 5‑die roll, convert it to a categorical
# variable, and plot the resulting distribution as a bar chart.
#
# 2. Topics Covered
# - Generating full factorial combinations with expand_grid()
# - Exact sampling distributions (no randomness)
# - Computing sample statistics (mean)
# - Categorical binning and frequency bar plots
# ============================================

# 3. Python Script

# Expand a grid representing five 8-sided dice
dice = expand_grid(
    {
        "die1": [1, 2, 3, 4, 5, 6, 7, 8],
        "die2": [1, 2, 3, 4, 5, 6, 7, 8],
        "die3": [1, 2, 3, 4, 5, 6, 7, 8],
        "die4": [1, 2, 3, 4, 5, 6, 7, 8],
        "die5": [1, 2, 3, 4, 5, 6, 7, 8]
    }
)

# Add a column of mean rolls and convert to a categorical
dice["mean_roll"] = (
    dice["die1"] +
    dice["die2"] +
    dice["die3"] +
    dice["die4"] +
    dice["die5"]
) / 5

dice["mean_roll"] = dice["mean_roll"].astype("category")

# Draw a bar plot of mean_roll
dice["mean_roll"].value_counts(sort=False).plot(kind="bar")
plt.show()

# ============================================
# 4. Additional Notes
# Exact sampling distribution
# - With 5 dice and 8 possible outcomes each, the total number of possible
#   outcomes is 8^5 = 32,768 — small enough to enumerate exhaustively.
# - This gives the *true* sampling distribution of the mean, without
#   relying on simulation (Monte Carlo).
# - Each bar height shows how frequently a particular mean occurs across
#   all possible combinations.
#
# Interpretation:
# - This distribution is discrete, not continuous.
# - Means cluster near the center because there are more combinations
#   producing values around the expected mean (4.5).
# - This demonstrates how sample statistics behave when *all possible
#   samples* are considered rather than random draws.
# ============================================
