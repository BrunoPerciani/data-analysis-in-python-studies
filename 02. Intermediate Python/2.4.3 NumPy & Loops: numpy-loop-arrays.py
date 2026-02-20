# ============================================
# 1. Task Description
# Loop over NumPy arrays of different dimensions. For a 1D array,
# iterate directly over its elements; for a 2D NumPy array, use
# np.nditer() to iterate over each individual element. This is
# useful when processing structured numeric data like baseball
# player heights and weights.
#
# 2. Topics Covered
# - Iterating over 1D NumPy arrays
# - Iterating over multi-dimensional arrays with np.nditer()
# - Type casting and formatted printing
# ============================================

# 3. Python Script

# Import numpy as np
import numpy as np

# For loop over 1D NumPy array np_height
for height in np_height:
    print(str(height) + " inches")

# For loop over 2D NumPy array np_baseball
# np.nditer allows iteration over every element in a multi-dimensional array
for baseball in np.nditer(np_baseball):
    print(str(baseball))

# ============================================
# 4. Additional Notes
# - For a 1D array, looping is straightforward: each iteration gives a scalar.
# - For a 2D array, looping directly gives *rows* (1D arrays). To get every
#   element individually, use np.nditer().
# - You can reshape arrays if needed:
#       np_height.reshape(-1, 1)
# - Vectorized operations are usually preferred over loops for performance:
#       np_height * 2 or np_baseball[:, 0] + 10
# ============================================
