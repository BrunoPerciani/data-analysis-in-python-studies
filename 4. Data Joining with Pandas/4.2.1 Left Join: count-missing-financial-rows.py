# ============================================
# 1. Task Description
# Use a left join to identify movies that are missing financial data.
# The goal is to merge the movies and financials tables on 'id' and
# count how many rows in the financial columns are missing as a result.
#
# 2. Topics Covered
# - Left joins with .merge(how="left")
# - Identifying missing rows after merging
# - Counting missing values with .isna().sum()
# ============================================

# 3. Python Script

# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on="id", how="left")

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials["budget"].isna().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

# ============================================
# 4. Additional Notes
# Counting missing rows with left join
# A left join keeps ALL rows from the left table (movies), while only
# matching rows from financials are included. This allows you to:
# - Identify movies with incomplete or missing financial data.
# - Quickly check how many movies lack budget or revenue information.
#
# After merging:
# - Missing financial rows appear as NaN in the financial columns.
# - .isna().sum() counts how many of these missing values exist.
#
# Context:
# The DataFrames `movies` and `financials` are preloaded.
# pandas is already imported as pd.
# ============================================
