# ============================================
# 1. Task Description
# Create a new categorical column, "Duration_Category", based on regex
# patterns that bucket text-based flight durations into Short-haul,
# Medium, Long-haul, or a default catch-all ("Extreme duration").
# Then, visualize the frequency of each category with a count plot.
#
# 2. Topics Covered
# - Building boolean conditions with .str.contains()
# - Vectorized conditional assignment with numpy.select
# - Visualizing category frequencies with seaborn.countplot
# ============================================

# 3. Python Script

# Create conditions for values in flight_categories to be created
conditions = [
    (planes["Duration"].str.contains(short_flights, regex=True, na=False)),
    (planes["Duration"].str.contains(medium_flights, regex=True, na=False)),
    (planes["Duration"].str.contains(long_flights, regex=True, na=False))
]

# Apply the conditions list to the flight_categories
planes["Duration_Category"] = np.select(
    conditions,
    flight_categories,
    default="Extreme duration"
)

# Plot the counts of each category
sns.countplot(data=planes, x="Duration_Category")
plt.show()

# ============================================
# 4. Additional Notes
# - The regex patterns are anchored to the start of the string to match
#   the hours portion (e.g., "5h 25m") reliably.
# - `na=False` ensures .str.contains returns False for missing values
#   instead of NaN, preventing errors in condition evaluation.
# - The default "Extreme duration" bucket captures any durations outside
#   the specified hour ranges (e.g., >16h or formats that don’t start
#   with an hours component). You can refine this rule as needed.
# - For consistent ordering in plots/groupbys, consider converting the
#   new column to an ordered Categorical with:
#       pd.Categorical(planes["Duration_Category"],
#                      categories=["Short-haul","Medium","Long-haul","Extreme duration"],
#                      ordered=True)
# ============================================
