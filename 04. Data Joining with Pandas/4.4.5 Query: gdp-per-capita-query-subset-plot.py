# ============================================
# 1. Task Description
# Merge GDP and population by country and date using an ordered merge with
# forward-fill, compute GDP per capita, pivot to a wide format (date as
# index, countries as columns), subset rows with .query(), and plot the
# recent series.
#
# 2. Topics Covered
# - Ordered merges with pd.merge_ordered() and forward-fill
# - Creating derived metrics (GDP per capita)
# - Pivoting to wide format with .pivot_table()
# - Subsetting rows using .query()
# - Plotting multiple time series
# ============================================

# 3. Python Script

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=["country", "date"], fill_method="ffill")

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop["gdp_per_capita"] = gdp_pop["gdp"] / gdp_pop["pop"]

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table("gdp_per_capita", "date", "country")

# Select dates equal to or greater than 1991-01-01 using .query()
# (reset the index so 'date' is a column visible to .query(), then set it back)
recent_gdp_pop = (
    gdp_pivot.reset_index()
             .query('date >= "1991-01-01"')
             .set_index("date")
)

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()

# ============================================
# 4. Additional Notes
# Subsetting rows with .query()
# - After pivoting, 'date' becomes the index. To use .query('date >= ...'),
#   reset the index to expose 'date' as a regular column, then set it back.
# - pd.merge_ordered() with fill_method="ffill" aligns different frequencies
#   (e.g., quarterly GDP vs yearly population) and carries forward the most
#   recent known values within each country–date panel.
#
# Assumptions:
# - DataFrames `gdp` and `pop` are loaded and contain 'country' and 'date'.
# - 'date' is a datetime64 column (use pd.to_datetime if needed).
# ============================================
