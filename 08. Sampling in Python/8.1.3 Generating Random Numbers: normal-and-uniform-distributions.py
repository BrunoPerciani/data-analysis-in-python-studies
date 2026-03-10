# ============================================
# 1. Task Description
# Generate random numbers from two different statistical distributions:
# - Uniform distribution defined on the interval [-3, 3]
# - Normal (Gaussian) distribution with mean 5 and standard deviation 2
# The goal is to practice generating synthetic data for simulation and
# visualization purposes.
#
# 2. Topics Covered
# - Random number generation with numpy
# - Uniform and normal distributions
# - Distribution‑specific arguments
# ============================================

# 3. Python Script

# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(low=-3, high=3, size=5000)

# Generate random numbers from a Normal(5, 2)
normals = np.random.normal(loc=5, scale=2, size=5000)

# Print normals
print(normals)

# ============================================
# 4. Additional Notes
# Generating random numbers
# - np.random.uniform(low, high, size) draws samples from a continuous
#   uniform distribution between the bounds [low, high].
# - np.random.normal(loc, scale, size) draws samples from a normal
#   distribution with mean = loc and standard deviation = scale.
# - Increasing size increases the smoothness of the sampled distribution
#   when plotted (e.g., with a histogram or KDE).
#
# Applications:
# - Simulations, bootstrapping, Monte Carlo methods
# - Testing algorithms on synthetic data
# - Visualizing theoretical distributions vs. empirical samples
#
# Context:
# numpy is loaded as np and matplotlib.pyplot as plt is available.
# ============================================
