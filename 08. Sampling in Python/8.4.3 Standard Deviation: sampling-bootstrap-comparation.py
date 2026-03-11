# ============================================
# 1. Task Description
# Compare the population standard deviation of track popularity with
# estimates derived from:
#   - the original sample
#   - the sampling distribution
#   - the bootstrap distribution
# This illustrates how well sampling‑based and bootstrap‑based methods
# approximate true population variability.
#
# 2. Topics Covered
# - Computing standard deviation (population vs. sample)
# - Using sampling distributions to estimate population SD
# - Using bootstrap distributions to estimate population SD
# - Understanding the scaling of standard errors by sqrt(n)
# ============================================

# 3. Python Script

# Calculate the population std dev popularity
pop_sd = spotify_population["popularity"].std(ddof=0)

# Calculate the original sample std dev popularity
samp_sd = spotify_sample["popularity"].std()

# Calculate the sampling dist'n estimate of std dev popularity
samp_distn_sd = np.std(sampling_distribution, ddof=1) * np.sqrt(5000)

# Calculate the bootstrap dist'n estimate of std dev popularity
boot_distn_sd = np.std(bootstrap_distribution, ddof=1) * np.sqrt(5000)

# Print the standard deviations
print([pop_sd, samp_sd, samp_distn_sd, boot_distn_sd])

# ============================================
# 4. Additional Notes
# Compare sampling and bootstrap standard deviations
# - pop_sd:
#       The true population standard deviation using all 40K+ Spotify tracks.
#
# - samp_sd:
#       The standard deviation computed from a single sample of size 5,000.
#       Typically underestimates (or occasionally overestimates) true SD.
#
# - samp_distn_sd:
#       Derived from the sampling distribution of sample means.
#       The standard deviation of sample means is the standard error:
#           SE = SD_pop / sqrt(n)
#       Therefore, multiplying the SE estimate by sqrt(n) gives an
#       estimate of SD_pop.
#
# - boot_distn_sd:
#       Same idea as above, but estimated via bootstrap resamples of size 5,000.
#       The bootstrap standard error estimate usually performs very well,
#       especially for larger samples.
#
# Interpretation:
# - Values close to pop_sd indicate that the method provides a good
#   approximation of the population variability.
# - Differences between samp_distn_sd and boot_distn_sd can reveal
#   how well the bootstrap mimics sampling‑distribution behavior.
#
# Context:
# spotify_population, spotify_sample, sampling_distribution, and
# bootstrap_distribution are pre‑loaded. numpy is imported as np.
# ============================================
