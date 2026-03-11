# ============================================
# 1. Task Description
# Quantify the variability of a point estimate (sample mean of Attrition)
# by repeatedly drawing simple random samples from the population and
# computing the sample mean each time. Visualize the sampling distribution
# of the mean using a histogram.
#
# 2. Topics Covered
# - Repeated sampling / replication
# - Sampling distribution of the mean
# - Visualizing variability due to sampling randomness
# ============================================

# 3. Python Script

# Create an empty list
mean_attritions = []

# Loop 500 times to create 500 sample means
for i in range(500):
    mean_attritions.append(
        attrition_pop.sample(n=60)["Attrition"].mean()
    )

# Create a histogram of the 500 sample means
plt.hist(mean_attritions, bins=16)
plt.show()

# ============================================
# 4. Additional Notes
# Replicating samples
# - Each sample mean varies because each draw includes a different set of rows.
# - The histogram approximates the sampling distribution of the mean.
# - By the Central Limit Theorem (CLT), with sufficiently large n, the
#   sampling distribution tends toward normality with:
#       mean  ≈ population mean
#       std   ≈ population std / sqrt(n)
#
# Context:
# pandas (pd) and matplotlib.pyplot (plt) are loaded.
# The DataFrame `attrition_pop` contains a numeric 'Attrition' column.
# ============================================
