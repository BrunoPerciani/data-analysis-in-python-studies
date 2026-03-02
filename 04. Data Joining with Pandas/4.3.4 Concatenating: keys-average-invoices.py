# ============================================
# 1. Task Description
# Concatenate monthly invoice tables and compute the average invoice
# total for each month using hierarchical keys. The goal is to analyze
# which month in the quarter had the highest average invoice total.
#
# 2. Topics Covered
# - Vertical concatenation with pd.concat()
# - Using keys to create MultiIndex levels
# - Grouping by index level
# - Visualizing aggregated data with a bar plot
# ============================================

# 3. Python Script

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat(
    [inv_jul, inv_aug, inv_sep],
    keys=["7Jul", "8Aug", "9Sep"]
)

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({"total": "mean"})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind="bar")
plt.show()

# ============================================
# 4. Additional Notes
# Concatenating with keys
# Using keys in pd.concat() creates a hierarchical index, making it easy
# to group data by the tables of origin—in this case, monthly invoice
# data for July, August, and September.
#
# Steps:
# - Concatenate monthly DataFrames with keys representing each month.
# - Group by the top-level index (the month key).
# - Compute the average invoice total per month.
# - Visualize the result using a bar plot to compare months.
#
# Context:
# The DataFrames `inv_jul`, `inv_aug`, and `inv_sep` contain invoice data
# for three consecutive months. pandas is imported as pd, and
# matplotlib.pyplot is imported as plt.
# ============================================
