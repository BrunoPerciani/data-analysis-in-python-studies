# ============================================
# 1. Task Description
# Compare the population mean popularity to estimates derived from:
#   - the original sample
#   - the sampling distribution of the mean
#   - the bootstrap distribution of the mean
# This demonstrates how sampling‑based and bootstrap‑based approaches
# approximate true population averages.
#
# 2. Topics Covered
# - Computing population and sample means
# - Estimating the mean using a sampling distribution
# - Estimating the mean using a bootstrap distribution
# - Understanding accuracy and convergence of mean estimators
# ============================================

# 3. Python Script

# Calculate the population mean popularity
pop_mean = spotify_population["popularity"].mean()

# Calculate the original sample mean popularity
samp_mean = spotify_sample["popularity"].mean()

# Calculate the sampling dist'n estimate of mean popularity
samp_distn_mean = np.mean(sampling_distribution)

# Calculate the bootstrap dist'n estimate of mean popularity
boot_distn_mean = np.mean(bootstrap_distribution)

# Print the means
print([pop_mean, samp_mean, samp_distn_mean, boot_distn_mean])

# ============================================
# 4. Additional Notes
# Compare sampling and bootstrap means
# - pop_mean:
#       The true population mean popularity across all ~40k Spotify tracks.
#
# - samp_mean:
#       The mean popularity computed from a random sample of size 5000.
#       Deviations from pop_mean reflect sampling variability.
#
# - samp_distn_mean:
#       The mean of the sampling distribution (i.e., many sample means).
#       By the Law of Large Numbers, this value should be very close to pop_mean.
#
# - boot_distn_mean:
#       The bootstrap equivalent — mean of many resample means.
#       Bootstrap distributions typically approximate population behavior
#       well when sample size is sufficiently large (n = 5000 here).
#
# Interpretation:
# - If samp_distn_mean and boot_distn_mean are close to pop_mean, it
#   indicates that both the sampling distribution and the bootstrap
#   distribution provide reliable estimators of the population mean.
# - samp_mean alone may deviate further simply due to random sampling
#   error from one specific sample.
#
# Context:
# pandas and numpy are loaded.
# The DataFrames/arrays:
#   - spotify_population
#   - spotify_sample
#   - sampling_distribution
#   - bootstrap_distribution
# are pre‑loaded.
# ============================================
