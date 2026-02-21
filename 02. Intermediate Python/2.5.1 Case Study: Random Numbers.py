# ============================================
# 1. Task Description
# Simulate a single move in the Empire State Building random-walk game.
# Roll a dice (integer from 1 to 6) and update your position (step):
#   • If dice <= 2  → move down 1 step
#   • If dice <= 5  → move up 1 step
#   • Otherwise     → move up a random number of steps (1 to 6)
#
# This exercise practices conditional logic using if/elif/else,
# and random number generation with NumPy.
#
# 2. Topics Covered
# - np.random.randint() for dice rolls
# - Conditional branching (if / elif / else)
# - Updating state based on random outcomes
# ============================================

# 3. Python Script

# NumPy is imported, seed is set elsewhere in the environment

# Starting step
step = 50

# Roll the dice (integer between 1 and 6)
dice = np.random.randint(1, 7)

# Determine next move based on dice roll
if dice <= 2:
    step = step - 1
elif dice <= 5:
    step = step + 1
else:
    # Roll again for random upward boost
    step = step + np.random.randint(1, 7)

# Print the dice outcome and the updated step
print(dice, step)

# ============================================
# 4. Additional Notes
# - np.random.randint(1, 7) returns numbers 1 through 6 inclusive.
# - This rule set will be used later to build full random-walk simulations.
# - You can prevent negative positions with:
#       step = max(0, step)
# ============================================
