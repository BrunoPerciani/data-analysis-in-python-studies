# ============================================
# 1. Task Description
# Merge quarterly GDP and yearly population data for multiple countries
# using pd.merge_ordered() with forward-fill to align different
# frequencies. The goal is to demonstrate how the *order* of merge keys
# affects both sorting and the forward-fill behavior.
#
# 2. Topics Covered
# - Time-aware ordered merges with pd.merge_ordered()
# - Merging on multiple keys (country, date)
# - Forward-filling missing values with fill_method="ffill"
# - Understanding how key order impacts sorted output and ffill results
# ============================================

# 3. Python Script

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(
    gdp,
    pop,
    on=("country", "date"),
    fill_method="ffill"
)

# Print date_ctry
print(date_ctry)

# ============================================
# 4. Additional Notes
# merge_ordered() caution, multiple columns
# When using pd.merge_ordered() with multiple columns and fill_method="ffill",
# the function first sorts by the provided keys *in the order given*.
# Forward-filling then proceeds along that sorted order.
#
# Implication:
# - If you specify on=("country", "date"), rows are sorted by country first,
#   then by date within each country, and ffill propagates within each
#   country's chronological sequence.
# - If you reverse the order (on=("date", "country")), the sort order
#   and the direction of ffill across rows change, which can inadvertently
#   carry values across countries at the same date (usually unintended).
#
# Context:
# - gdp: quarterly GDP series per country.
# - pop: yearly population series per country.
# - Using on=("country", "date") ensures ffill occurs within each country
#   over time, which is typically the desired behavior for panel time series.
# ============================================
