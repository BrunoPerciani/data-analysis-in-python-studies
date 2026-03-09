# ============================================
# 1. Task Description
# Use .groupby() with named aggregations to compute summary statistics for
# unemployment rates across continents. Specifically, calculate both the
# mean and standard deviation of the 2021 unemployment rate, returning a
# tidy summary DataFrame with clear column names.
#
# 2. Topics Covered
# - Using .groupby() to summarize data by category
# - Named aggregations inside .agg()
# - Computing mean and standard deviation for numeric columns
# ============================================

# 3. Python Script

continent_summary = unemployment.groupby("continent").agg(
    # Create the mean_rate_2021 column
    mean_rate_2021=("2021", "mean"),
    # Create the std_rate_2021 column
    std_rate_2021=("2021", "std")
)

print(continent_summary)

# ============================================
# 4. Additional Notes
# Named aggregations
# - Named aggregations allow you to assign custom, descriptive column
#   names directly inside .agg(), improving clarity of the resulting
#   DataFrame.
# - This avoids ambiguous column names when performing multiple
#   aggregations on the same original variable.
#
# Interpretation:
# - mean_rate_2021 shows the average unemployment for each continent.
# - std_rate_2021 shows the variability (spread) of unemployment within
#   each continent for the year 2021.
#
# Context:
# pandas is imported as pd.
# The DataFrame `unemployment` contains a 'continent' column and a '2021'
# unemployment rate column.
# ============================================
