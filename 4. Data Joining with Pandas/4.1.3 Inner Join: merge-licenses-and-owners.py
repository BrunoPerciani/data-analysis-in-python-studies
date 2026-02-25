# ============================================
# 1. Task Description
# Perform a one-to-many merge between the licenses and biz_owners tables
# to explore the most common business owner titles. Since a business may
# have multiple owners, merging on the 'account' column will produce
# repeated rows for businesses with more than one owner.
#
# 2. Topics Covered
# - One-to-many relationships in merges
# - Merging DataFrames using .merge()
# - Grouping and counting with .groupby().agg()
# - Sorting aggregated results
# ============================================

# 3. Python Script

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on="account")

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby("title").agg({"account": "count"})

# Sort the counted_df in descending order
sorted_df = counted_df.sort_values("account", ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

# ============================================
# 4. Additional Notes
# One-to-many merge
# In a one-to-many relationship, a record in the left table can match
# multiple records in the right table during the merge. As a result:
# - Rows from the left table may appear multiple times.
# - The merged DataFrame expands to include all matches.
#
# In this exercise:
# - `licenses` contains business license information.
# - `biz_owners` contains owner information, with one business potentially
#   having multiple owners.
# - Merging on 'account' expands rows accordingly.
# - Grouping by 'title' and counting accounts reveals which business
#   owner titles (e.g., CEO, Secretary, Vice President) appear most often.
#
# Context:
# pandas is imported as pd.
# The DataFrames `licenses` and `biz_owners` are already loaded.
# ============================================
