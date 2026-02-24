# ============================================
# 1. Task Description
# Load a CSV file into a pandas DataFrame and compute a competitive
# metric: involuntary bumps per 10,000 passengers by airline. The goal
# is to aggregate totals and derive a standardized rate.
#
# 2. Topics Covered
# - Reading CSV files with pd.read_csv()
# - Grouping and summing with .groupby().sum()
# - Creating derived metrics with vectorized arithmetic
# - Inspecting the resulting DataFrame
# ============================================

# 3. Python Script

# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())

airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = (
    airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000
)

# Print airline_totals
print(airline_totals)

# ============================================
# 4. Additional Notes
# CSV to DataFrame
# Reading a CSV into a DataFrame is a common first step in analysis.
# After loading, group by airline and sum the relevant columns to get
# totals across 2016–2017, then compute bumps per 10,000 passengers:
#     bumps_per_10k = nb_bumped / total_passengers * 10000
#
# Context:
# - pandas is imported as pd.
# - "airline_bumping.csv" is available in the working directory.
# ============================================
