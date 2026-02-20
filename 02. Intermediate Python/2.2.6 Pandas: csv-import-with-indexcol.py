# ============================================
# 1. Task Description
# Import data from a CSV file into a pandas DataFrame and ensure that
# the first column is used as the row index. Without specifying
# index_col, pandas treats the first column as a regular data column.
# Using index_col=0 correctly assigns it as row labels.
#
# 2. Topics Covered
# - pandas.read_csv()
# - index_col parameter to set custom row index
# - Basic DataFrame inspection using print()
# ============================================

# Import pandas as pd
import pandas as pd

# Fix the CSV import by specifying index_col=0 so the first column
# becomes the DataFrame index rather than a separate unnamed column
cars = pd.read_csv('cars.csv', index_col=0)

# Print the resulting DataFrame
print(cars)

# ============================================
# 4. Additional Notes
# - index_col=0 tells pandas to use the first column of the CSV
#   as the row index.
# - You can check the index afterwards with:
#       print(cars.index)
# - If the CSV has a named index column, pandas automatically
#   reads that name into cars.index.name.
# ============================================
