
# ============================================
# 1. Task Description
# Using the NYC schools SAT dataset, answer three questions:
# 1) Which schools have the best math results? (≥ 80% of 800 → ≥ 640)
# 2) What are the top 10 performing schools based on combined SAT scores?
# 3) Which single borough has the largest standard deviation in total SAT?
#
# 2. Topics Covered
# - Boolean filtering and sorting
# - Creating derived columns
# - Grouping and aggregating by categories
# - Selecting and renaming columns
# - Rounding numerical results
# ============================================

# 3. Python Script

# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...

# Which schools are best for math?
best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]].sort_values("average_math", ascending=False)
print(best_math_schools)

# Calculate total_SAT per school
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

# Who are the top 10 performing schools?
top_10_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT", ascending = False).head(10)
print(top_10_schools)

# Which NYC borough has the highest standard deviation for total_SAT?
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

# Filter for max std and make borough a column
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

# Rename the columns for clarity
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

# Optional: Move borough from index to column
largest_std_dev.reset_index(inplace=True)
print(largest_std_dev)

# Ensure the output contains only one row and correct columns (already rounded)
# If there are ties, this will include multiple rows; if needed, take the first:
# largest_std_dev = largest_std_dev.nlargest(1, "std_SAT")

# ============================================
# 4. Additional Notes
# - Best math schools:
#   Threshold is 80% of the maximum 800 points → 0.8 * 800 = 640.
# - top_10_schools:
#   Uses the sum of average_math, average_reading, and average_writing (total_SAT).
# - largest_std_dev:
#   Groups by borough, then computes count (num_schools), mean (average_SAT),
#   and standard deviation (std_SAT) of total_SAT; all values are rounded to 2 decimals.
#
# Assumptions:
# - The CSV file "schools.csv" exists in the working directory.
# - Columns present: "school_name", "borough", "average_math",
#   "average_reading", "average_writing".
# ============================================
