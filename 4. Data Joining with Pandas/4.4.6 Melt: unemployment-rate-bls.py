# ============================================
# 1. Task Description
# Reshape a wide-format unemployment rate table from the US Bureau of
# Labor Statistics (BLS) into a long/tidy format using .melt(), create
# a proper date column, sort chronologically, and plot the unemployment
# rate over time.
#
# 2. Topics Covered
# - Reshaping with .melt()
# - Constructing a datetime column from month/year parts
# - Sorting time series data
# - Plotting a line chart over time
# ============================================

# 3. Python Script

# Unpivot everything besides the year column
ur_tall = ur_wide.melt(
    id_vars=["year"], 
    var_name="month", 
    value_name="unempl_rate"
)

# Create a date column using the month and year columns of ur_tall
# (BLS months are typically abbreviated English month names, e.g., 'Jan')
ur_tall["date"] = pd.to_datetime(
    ur_tall["month"] + "-" + ur_tall["year"].astype(str),
    format="%b-%Y",
    errors="coerce"
)

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values("date")

# Plot the unempl_rate by date
ur_sorted.plot(x="date", y="unempl_rate")
plt.show()

# ============================================
# 4. Additional Notes
# Using .melt() to reshape government data
# BLS often publishes data with one column per month and one row per year.
# Melting converts this wide layout to a tidy long format, which is easier
# to filter, aggregate, and visualize over time.
#
# Tips:
# - Ensure 'year' is treated as string when concatenating with month names.
# - Use an explicit datetime format (e.g., '%b-%Y') so parsing is reliable.
# - After melting and parsing dates, sort by the new 'date' column before plotting.
#
# Assumptions:
# - The DataFrame `ur_wide` is loaded with columns: 'year', 'Jan', 'Feb', ..., 'Dec'.
# - pandas is imported as pd and matplotlib.pyplot as plt.
# ============================================
