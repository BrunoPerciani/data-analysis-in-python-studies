# ============================================
# 1. Task Description
# Extract the year component from a date column and create a pivot table
# showing the average temperature for each city across different years.
# The goal is to analyze long-term temperature trends by city and year.
#
# 2. Topics Covered
# - Extracting date components with .dt.year
# - Adding new columns to a DataFrame
# - Creating pivot tables with .pivot_table()
# - Grouping data by multiple index levels
# ============================================

# 3. Python Script

# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(
    values="avg_temp_c",
    index=("country", "city"),
    columns="year"
)

# See the result
print(temp_by_country_city_vs_year)

# ============================================
# 4. Additional Notes
# Pivot temperature by city and year
# Looking at temperature data across years—rather than months—helps
# simplify long-term trend analysis.
#
# Tips:
# - Access date components with dataframe["column"].dt.component
#     Examples:
#       dataframe["date"].dt.month
#       dataframe["date"].dt.day
#       dataframe["date"].dt.year
#
# - Pivot tables summarize data using a combination of index variables
#   (country, city) and columns (year). This creates a compact view of
#   temperature trends over time.
#
# Context:
# pandas has been imported as pd, and `temperatures` is available with
# columns including "date" and "avg_temp_c".
# ============================================
