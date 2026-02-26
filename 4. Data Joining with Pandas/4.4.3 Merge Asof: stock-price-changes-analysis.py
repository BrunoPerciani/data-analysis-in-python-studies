# ============================================
# 1. Task Description
# Merge three irregularly sampled stock price logs (JPM, WFC, BAC) using
# time-aware as-of merges so all series align on timestamps. Then compute
# price changes over time with .diff() and plot the results for review.
#
# 2. Topics Covered
# - Time-based alignment with pd.merge_asof()
# - Handling near-synchronous timestamps (direction="nearest")
# - Computing period-over-period changes with .diff()
# - Plotting multiple series together
# ============================================

# 3. Python Script

# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(
    jpm, wells,
    on="date_time",
    suffixes=("", "_wells"),
    direction="nearest"
)

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(
    jpm_wells, bac,
    on="date_time",
    suffixes=("_jpm", "_bac"),
    direction="nearest"
)

# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=["close_jpm", "close_wells", "close_bac"])
plt.show()

# ============================================
# 4. Additional Notes
# Using merge_asof() to study stocks
# When logs are sampled at irregular/near-regular intervals (e.g., ~5 min
# with latency), pd.merge_asof() aligns records by nearest timestamp,
# preserving chronological order without creating cartesian products.
#
# Steps:
# - As-of merge JPM with WFC on 'date_time' (nearest timestamps).
# - As-of merge the result with BAC similarly.
# - Compute first differences with .diff() to analyze price changes.
# - Plot the three 'close' deltas to visually compare co-movement.
#
# Context:
# The DataFrames `jpm`, `wells`, and `bac` contain columns 'date_time'
# and 'close' (among others). pandas is imported as pd, and
# matplotlib.pyplot is imported as plt.
# ============================================
