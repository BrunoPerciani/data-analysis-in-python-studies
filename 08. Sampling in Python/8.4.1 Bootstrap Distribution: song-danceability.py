# ============================================
# 1. Task Description
# Generate a bootstrap distribution for the mean danceability using a
# sampled subset of the Spotify dataset. Resample the given sample
# (spotify_sample) with replacement many times, compute the mean
# danceability for each resample, and visualize the bootstrap distribution
# with a histogram.
#
# 2. Topics Covered
# - Bootstrap resampling (with replacement) from a sample
# - Computing a summary statistic on each resample
# - Visualizing the bootstrap distribution
# ============================================

# 3. Python Script

# Replicate this 1000 times
mean_danceability_1000 = []
for i in range(1000):
    mean_danceability_1000.append(
        np.mean(spotify_sample.sample(frac=1, replace=True)["danceability"])
    )

# Draw a histogram of the resample means
plt.hist(mean_danceability_1000)
plt.show()

# ============================================
# 4. Additional Notes
# Generating a bootstrap distribution
# - Sampling distribution: sample from the population (usually without replacement),
#   compute the statistic, and replicate — used to understand variability across
#   *different* random samples from the population.
# - Bootstrap distribution: resample the *observed sample* with replacement,
#   compute the statistic for each resample, and replicate — used to estimate the
#   variability (and confidence intervals) of the statistic when only a sample is available.
#
# Tips:
# - Set a random seed (e.g., np.random.seed(2022)) for reproducibility.
# - You can compute a 95% bootstrap CI via percentiles, e.g.:
#       np.percentile(mean_danceability
