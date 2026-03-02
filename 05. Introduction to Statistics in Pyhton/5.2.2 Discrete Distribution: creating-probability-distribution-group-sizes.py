# ============================================
# 1. Task Description
# Create a probability distribution for restaurant group sizes, compute
# the expected value of group size, and calculate the probability that a
# randomly selected group has size 4 or more.
#
# 2. Topics Covered
# - Building probability distributions from value counts
# - Computing expected value as sum(outcome * probability)
# - Subsetting by condition and summing probabilities
# ============================================

# 3. Python Script

# Create probability distribution
size_dist = restaurant_groups["group_size"].value_counts() / restaurant_groups.shape[0]

# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ["group_size", "prob"]

# Expected value
expected_value = np.sum(size_dist["group_size"] * size_dist["prob"])

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist["group_size"] >= 4]

# Sum the probabilities of groups_4_or_more
prob_4_or_more = np.sum(groups_4_or_more["prob"])
print(prob_4_or_more)

# ============================================
# 4. Additional Notes
# Creating a probability distribution
# - The probability of each group size is the frequency of that size divided
#   by the total number of groups (here, 10).
# - Expected value is computed as Σ (size * probability).
# - Summing probabilities over sizes ≥ 4 yields the chance that a randomly
#   selected group has size 4 or more.
#
# Context:
# pandas is imported as pd, numpy as np, and matplotlib.pyplot as plt.
# The DataFrame `restaurant_groups` contains a column 'group_size'.
# ============================================
