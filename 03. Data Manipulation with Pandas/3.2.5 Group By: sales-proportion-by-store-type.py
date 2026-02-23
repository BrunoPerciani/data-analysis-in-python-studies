# ============================================
# 1. Task Description
# Calculate the percentage of total weekly sales contributed by each
# store type (A, B, C) without using .groupby(). The goal is to compute
# totals by type via boolean filtering and then derive proportions of the
# overall sales.
#
# 2. Topics Covered
# - Filtering rows by category (type == "A"/"B"/"C")
# - Summing a column with .sum()
# - Computing proportions of totals
# - Displaying the result
# ============================================

# 3. Python Script

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
# (Use a pandas Series so division works elementwise)
sales_propn_by_type = pd.Series([sales_A, sales_B, sales_C], index=["A", "B", "C"]) / sales_all
print(sales_propn_by_type)

# ============================================
# 4. Additional Notes
# What percent of sales occurred at each store type?
# You can compute grouped summaries without .groupby() by using boolean
# filters and .sum(). After summing weekly_sales for each type, divide
# by the total to obtain proportions.
#
# Context:
# - Walmart store types are encoded as:
#   A = supercenters, B = discount stores, C = neighborhood markets.
# - The DataFrame `sales` is available and pandas is imported as pd.
#
# Tip:
# - Creating a pandas Series (rather than a Python list) enables
#   elementwise division when computing proportions.
# ============================================
