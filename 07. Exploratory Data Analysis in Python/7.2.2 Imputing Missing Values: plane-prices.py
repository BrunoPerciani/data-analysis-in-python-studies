# ============================================
# 1. Task Description
# Impute missing plane ticket prices by replacing them with the median
# ticket price for each airline. This method preserves differences 
# between airlines and avoids distortions caused by global medians.
#
# 2. Topics Covered
# - Grouping and computing medians with .groupby()
# - Converting a Series to a dictionary
# - Mapping grouped statistics back to the DataFrame
# - Imputing missing values with .fillna()
# ============================================

# 3. Python Script

# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()
print(airline_prices)

# Convert to a dictionary
prices_dict = airline_prices.to_dict()

# Map the dictionary to the missing values
planes["Price"] = planes["Price"].fillna(planes["Airline"].map(prices_dict))

# Check for missing values
print(planes.isna().sum())

# ============================================
# 4. Additional Notes
# Imputing missing plane prices
# - Instead of dropping rows with missing prices, imputing them preserves
#   valuable data and avoids reducing sample size.
# - Using the median per airline is more robust than using the global
#   median because:
#       • Price levels vary significantly across airlines.
#       • The median resists the influence of extreme ticket prices.
# - Mapping the airline-specific medians back into the DataFrame ensures
#   accurate, tailored imputation.
#
# Interpretation:
# - After imputation, there should be zero missing values left in the 
#   "Price" column.
# - The distribution of prices remains realistic and consistent with 
#   airline-level trends observed in earlier visualizations.
#
# Context:
# pandas is imported as pd.
# The DataFrame `planes` contains 'Airline' and 'Price', with some missing 
# price values and the 'Additional_Info' column already removed earlier.
# ============================================
