# ============================================
# 1. Task Description
# Calculate a point estimate (sample statistic) for the proportion of late
# shipments in the late_shipments dataset. Each row represents one delivery,
# and the goal is to estimate how often deliveries arrive late.
#
# 2. Topics Covered
# - Computing proportions from categorical data
# - Boolean comparisons in pandas
# - Interpreting the sample mean as a proportion
# ============================================

# 3. Python Script

# Print the late_shipments dataset
print(late_shipments)

# Calculate the proportion of late shipments
late_prop_samp = (late_shipments["late"] == "Yes").mean()

# Print the results
print(late_prop_samp)

# ============================================
# 4. Additional Notes
# Calculating the sample mean
# - When working with binary or categorical indicators, a proportion can
#   be calculated by evaluating a Boolean condition and taking the mean:
#       (df["col"] == "Yes").mean()
# - In pandas:
#       True → 1
#       False → 0
#   so the mean of a Boolean Series equals the proportion of True values.
#
# Interpretation:
# - late_prop_samp represents the estimated probability that a randomly
#   selected shipment from this sample was delivered late.
# - This is a point estimate of the true population proportion of late
#   shipments.
#
# Context:
# pandas is loaded as pd.
# The DataFrame `late_shipments` contains a column named "late" with
# values "Yes" or "No".
# ============================================
