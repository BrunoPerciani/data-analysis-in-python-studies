# ============================================
# 1. Task Description
# Create a categorical variable "Duration_Category" from a string-based
# "Duration" column in the planes dataset. The goal is to group flights
# into three buckets based on the total hours reported in the duration
# string: "Short-haul" (0–4h), "Medium" (5–9h), and "Long-haul" (10–16h).
#
# 2. Topics Covered
# - Building categorical buckets from text durations
# - Using regex patterns with .str.contains()
# - Vectorized conditional assignment with numpy.select
# - Preserving category order with pandas.Categorical
# ============================================

# 3. Python Script

# Create a list of categories
flight_categories = ["Short-haul", "Medium", "Long-haul"]

# Create short_flights
short_flights = r"^(0h|1h|2h|3h|4h)"

# Create medium_flights
medium_flights = r"^(5h|6h|7h|8h|9h)"

# Create long_flights
long_flights = r"^(10h|11h|12h|13h|14h|15h|16h)"

# Build boolean masks using the patterns on the "Duration" column
short_mask = planes["Duration"].str.contains(short_flights, regex=True, na=False)
medium_mask = planes["Duration"].str.contains(medium_flights, regex=True, na=False)
long_mask = planes["Duration"].str.contains(long_flights, regex=True, na=False)

# Assign categories with np.select (unmatched rows become NaN)
import numpy as np
planes["Duration_Category"] = np.select(
    condlist=[short_mask, medium_mask, long_mask],
    choicelist=flight_categories,  # matches order: Short-haul, Medium, Long-haul
    default=np.nan
)

# (Optional) Make it an ordered categorical for downstream plotting/analysis
import pandas as pd
planes["Duration_Category"] = pd.Categorical(
    planes["Duration_Category"],
    categories=flight_categories,
    ordered=True
)

# Quick check (value counts per bucket)
print(planes["Duration_Category"].value_counts(dropna=False))

# ============================================
# 4. Additional Notes
# - The regexes anchor at the start (^) because typical entries begin with
#   the hour component, e.g., "5h 25m". This avoids accidental matches in
#   the minutes portion.
# - Entries like "19h" will be categorized only if included in the pattern
#   range; adjust the long_flights pattern to extend beyond 16h if needed.
# - If you encounter durations without an hours part (e.g., "45m"), they
#   won’t match any pattern and will result in NaN. You can handle these by
#   adding another pattern (e.g., r"^\d{1,2}m$") and mapping them to
#   "Short-haul" or a custom bucket, depending on your business rule.
# - Converting to an ordered Categorical helps keep plots and groupby
#   outputs in
