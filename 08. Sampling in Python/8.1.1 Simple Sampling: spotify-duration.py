# ============================================
# 1. Task Description
# Draw a simple random sample of 1000 songs from the Spotify population
# dataset and compare the mean duration (in minutes) of the sample to 
# the mean duration of the entire population.
#
# 2. Topics Covered
# - Random sampling with pandas .sample()
# - Computing means of numeric columns
# - Comparing sample vs. population statistics
# ============================================

# 3. Python Script

# Sample 1000 rows from spotify_population
spotify_sample = spotify_population.sample(n=1000)

# Print the sample
print(spotify_sample)

# Calculate the mean duration in mins from spotify_population
mean_dur_pop = spotify_population["duration_minutes"].mean()

# Calculate the mean duration in mins from spotify_sample
mean_dur_samp = spotify_sample["duration_minutes"].mean()

# Print the means
print(mean_dur_pop)
print(mean_dur_samp)

# ============================================
# 4. Additional Notes
# Simple sampling with pandas
# - .sample(n=...) performs simple random sampling without replacement 
#   unless explicitly specified otherwise.
# - Comparing the sample mean to the population mean helps assess how 
#   representative the sample is.
# - With a large population (~40k songs), a sample of 1000 is generally
#   expected to produce a mean reasonably close to the population mean.
#
# Context:
# pandas is loaded as pd.
# The DataFrame `spotify_population` contains song-level data including
# 'duration_minutes'.
# ============================================
