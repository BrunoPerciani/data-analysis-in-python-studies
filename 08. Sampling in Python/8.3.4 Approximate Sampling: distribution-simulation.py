# ============================================
# 1. Task Description
# Generate an approximate sampling distribution for the mean of five
# eight‑sided dice (values 1–8) by simulation. Repeat the process many
# times (here, 1000) and visualize the distribution of the simulated
# sample means.
#
# 2. Topics Covered
# - Monte Carlo simulation for sampling distributions
# - Repeated sampling and computing a sample statistic
# - Visualizing the simulated sampling distribution with a histogram
# ============================================

# 3. Python Script

# Replicate the sampling code 1000 times
sample_means_1000 = []
for i in range(1000):
    sample_means_1000.append(
        np.random.choice(list(range(1, 9)), size=5, replace=True).mean()
    )

# Draw a histogram of sample_means_1000 with 20 bins
plt.hist(sample_means_1000, bins=20)
plt.show()

# ============================================
# 4. Additional Notes
# Generating an approximate sampling distribution
# - When exact enumeration is infeasible or cumbersome, simulate the
#   sampling process to approximate the sampling distribution.
# - With five d8 rolls, the expected mean is 4.5; as the number of
#   replications increases (e.g., 10,000+), the simulated distribution
#   will better approximate the true distribution and center near 4.5.
# - Increasing the number of replications and the number of dice (n)
#   tends to make the distribution of the mean more bell‑shaped due to
#   the Central Limit Theorem.
#
# Tips:
# - For reproducibility, set a seed with np.random.seed(<integer>).
# - You can compare this approximate histogram to the exact distribution
#   obtained by enumerating all 8^5 outcomes (as done in the previous task).
# ============================================
