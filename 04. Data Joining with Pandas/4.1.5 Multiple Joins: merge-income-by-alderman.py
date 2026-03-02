# ============================================
# 1. Task Description
# Perform a three-DataFrame merge to enrich business license data with
# demographic information (median income by ZIP code) and political
# boundaries (wards/aldermen). The goal is to compute the median income
# by alderman after merging the datasets.
#
# 2. Topics Covered
# - Chaining multiple .merge() operations
# - Joining on different keys across tables (zip and ward)
# - Grouping and aggregating with .groupby().agg()
# - Summarizing results by a categorical variable (alderman)
# ============================================

# 3. Python Script

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = (
    licenses.merge(zip_demo, on="zip")
            .merge(wards, on="ward")
)

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby("alderman").agg({"income": "median"}))

# ============================================
# 4. Additional Notes
# Three table merge
# Merging multiple tables allows you to combine business attributes
# (licenses), geographic/political context (wards), and socioeconomic
# indicators (zip_demo with median income).
#
# Steps:
# 1) licenses ⨝ zip_demo on 'zip' to add income by ZIP code.
# 2) (licenses ⨝ zip_demo) ⨝ wards on 'ward' to add alderman info.
# 3) Group by 'alderman' and compute median 'income'.
#
# Context:
# The DataFrames `licenses`, `wards`, and `zip_demo` are preloaded.
# pandas is imported as pd.
# ============================================
