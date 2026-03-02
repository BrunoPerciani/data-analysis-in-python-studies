# ============================================
# 1. Task Description
# Merge US GDP and S&P 500 returns using an ordered merge keyed on time,
# forward-fill missing values from the S&P 500 series to align with GDP
# dates, then compute the correlation between GDP and returns.
#
# 2. Topics Covered
# - Ordered time-based merges with pd.merge_ordered()
# - Handling missing values with forward-fill (fill_method="ffill")
# - Subsetting columns
# - Computing correlations with .corr()
# ============================================

# 3. Python Script

# Use merge_ordered() to merge gdp and sp500, and forward fill missing values
gdp_sp500 = pd.merge_ordered(
    gdp, sp500, left_on="year", right_on="date",
    how="left", fill_method="ffill"
)

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[["gdp", "returns"]]

# Print gdp_returns correlation
print(gdp_returns.corr())

# ============================================
# 4. Additional Notes
# Correlation between GDP and S&P500
# When combining macroeconomic indicators with market data, aligning on a
# time axis is crucial. pd.merge_ordered() preserves chronological order
# and supports forward-filling, which is useful when one dataset (e.g.,
# monthly/quarterly GDP) does not align perfectly with another (e.g.,
# daily/weekly returns).
#
# Steps:
# - Perform a left ordered merge keyed on year/date.
# - Forward-fill S&P 500 returns to match GDP timestamps.
# - Compute the correlation matrix between GDP and returns.
#
# Context:
# The DataFrames `gdp` (with a 'year' column) and `sp500` (with 'date'
# and 'returns' columns) are preloaded. pandas is imported as pd.
# ============================================
