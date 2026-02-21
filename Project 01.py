# ============================================
# 1. Task Description
# Perform exploratory data analysis on Netflix movie data to:
#   • filter to Movies from the 1990s (1990 <= release_year < 2000),
#   • visualize the distribution of movie durations in that decade,
#   • save an approximate most frequent duration into `duration`,
#   • count how many Action movies are "short" (< 90 minutes) and
#     save the result into `short_movie_count`.
#
# 2. Topics Covered
# - pandas filtering and boolean masks (decade subsetting)
# - exploratory plotting (histogram with matplotlib)
# - counting via iteration and via vectorized boolean sums
# - chainable, readable DataFrame operations
# ============================================

# 3. Python Script

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter the to keep only movies released in the 1990s
# Start by filtering out movies that were released in or after 1990
subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]

# And then do the same to filter out movies released before 2000
movies_1990s = subset[(subset["release_year"] < 2000)]

# Another way to do this step is to use the & operator which allows you to do this type of filtering in one step
# movies_1990s = netflix_subset[(netflix_subset["release_year"] >= 1990) & (netflix_subset["release_year"] < 2000)]

# Visualize the duration column of your filtered data to see the distribution of movie durations
# See which bar is the highest and save the duration value, this doesn't need to be exact!
plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

duration = 100

# Filter the data again to keep only the Action movies
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Use a for loop and a counter to count how many short action movies there were in the 1990s

# Start the counter
short_movie_count = 0

# Iterate over the labels and rows of the DataFrame and check if the duration is less than 90, if it is, add 1 to the counter, if it isn't, the counter should remain the same
for label, row in action_movies_1990s.iterrows() :
    if row["duration"] < 90 :
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)

# A quicker way of counting values in a column is to use .sum() on the desired column
# (action_movies_1990s["duration"] < 90).sum()

# ============================================
# 4. Additional Notes
# - If you prefer a *programmatic* mode estimate (instead of eyeballing),
#   you could bin durations with numpy and take the bin center with max count,
#   or use pandas' value_counts().idxmax() on integer-rounded durations:
#       duration = movies_1990s["duration"].round().value_counts().idxmax()
# - Vectorized counting with `.sum()` on a boolean mask is the idiomatic
#   and efficient approach in pandas; prefer it over iterrows() for scale.
# - Consider handling missing durations:
#       movies_1990s = movies_1990s.dropna(subset=["duration"])
# ============================================
