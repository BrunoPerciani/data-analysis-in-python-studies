# ============================================
# 1. Task Description
# Iterate over a list of lists where each inner list contains the
# name of a room and its area in square meters. For each room,
# print a formatted sentence describing its name and area.
#
# 2. Topics Covered
# - Looping over nested lists
# - Accessing elements inside sublists
# - String concatenation and type casting
# ============================================

# 3. Python Script

# House list of lists: each sublist contains [room_name, area_in_sqm]
house = [
    ["hallway", 11.25],
    ["kitchen", 18.0],
    ["living room", 20.0],
    ["bedroom", 10.75],
    ["bathroom", 9.50]
]

# Build a for loop to print room information
forthe " + room[0] + " is " + str(room[1]) + " sqm")

# ============================================
# 4. Additional Notes
# - `room[0]` accesses the room name; `room[1]` accesses the area.
# - A cleaner modern alternative uses f-strings:
#       print(f"The {room[0]} is {room[1]} sqm")
# - Nested lists are a simple data structure; pandas DataFrames or
#   dictionaries are often better for real-world use cases.
# ============================================
