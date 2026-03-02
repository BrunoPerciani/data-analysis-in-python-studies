# ============================================
# 1. Task Description
# Reshape the US 10-year treasury bond percent-change table from wide to
# long format using .melt(), filter to keep only the "close" metric, then
# merge it with the Dow Jones Industrial (DJI) percent-change table.
# Finally, plot both series to visually compare stock vs. bond behavior.
#
# 2. Topics Covered
# - Reshaping wide-to-long with .melt()
# - Filtering rows using .query()
# - Time-aware ordered merging with pd.merge_ordered()
# - Plotting multiple time series for comparison
# ============================================

# 3. Python Script

# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars="metric", var_name="date", value_name="close")

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric == "close"')

# (Optional) Ensure date is datetime if needed
# bond_perc_close["date"] = pd.to_datetime(bond_perc_close["date"])
# dji["date"] = pd.to_datetime(dji["date"])

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(
    dji, bond_perc_close, on="date", suffixes=("_dow", "_bond"), how="inner"
)

# Plot only the close_dow and close_bond columns
dow_bond.plot(y=["close_dow", "close_bond"], x="date", rot=90)
plt.show()

# ============================================
# 4. Additional Notes
# Using .melt() for stocks vs bond performance
# - The ten_yr table is wide with one column per year; .melt() converts it
#   to a tidy long format (date, close).
# - .query() cleanly filters to the "close" metric for bonds.
# - pd.merge_ordered() aligns the two time series by date while preserving
#   ordering; using how="inner" keeps dates present in both tables.
# - Plotting both series together helps visualize the typical inverse
#   relationship between stock and bond price changes.
#
# Assumptions:
# - DataFrames `ten_yr` (with a 'metric' column and year columns) and
#   `dji` (with 'date' and 'close') are loaded.
# - pandas is imported as pd and matplotlib.pyplot as plt.
# - Convert 'date' columns to datetime if they are strings for accurate plotting.
# ============================================
