# ============================================
# 1. Task Description
# Merge ridership, calendar, and station metadata to compute the total
# number of rides passing through Wilson station on weekdays in July.
# The goal is to join multiple tables and filter rows by specific
# conditions (month, day_type, station_name), then sum the rides.
#
# 2. Topics Covered
# - Merging multiple DataFrames with .merge()
# - Applying multi-condition boolean filters
# - Selecting a single column with .loc[]
# - Aggregating with .sum()
# ============================================

# 3. Python Script

# Merge the ridership, cal, and stations tables
ridership_cal_stations = (
    ridership.merge(cal, on=["year", "month", "day"])
             .merge(stations, on="station_id")
)

# Create a filter to filter ridership_cal_stations
filter_criteria = (
    (ridership_cal_stations["month"] == 7)
    & (ridership_cal_stations["day_type"] == "Weekday")
    & (ridership_cal_stations["station_name"] == "Wilson")
)

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, "rides"].sum())

# ============================================
# 4. Additional Notes
# Total riders in a month
# This example demonstrates how to bring together fact data (ridership),
# a calendar table (cal), and station attributes (stations) to answer a
# time- and location-specific question.
#
# Steps:
# - Merge ridership with cal on (year, month, day) to attach day_type.
# - Merge the result with stations on station_id to access station_name.
# - Filter to July (month == 7), weekdays (day_type == "Weekday"),
#   and the Wilson station (station_name == "Wilson").
# - Sum the rides column for the filtered subset to get the total.
#
# Context:
# The DataFrames `cal`, `ridership`, and `stations` are preloaded.
# pandas is imported as pd.
# ============================================
