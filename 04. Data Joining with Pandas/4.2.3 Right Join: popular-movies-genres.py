# ============================================
# 1. Task Description
# Determine the genres of the most popular movies by merging the
# movie_to_genres table with the pop_movies table using a right join.
# Then count the number of movies per genre and visualize the result.
#
# 2. Topics Covered
# - Right joins using .merge(how="right")
# - Handling columns with different key names (movie_id vs id)
# - Grouping and counting with .groupby().agg()
# - Bar chart visualization with .plot(kind="bar")
# ============================================

# 3. Python Script

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(
    pop_movies,
    how="right",
    left_on="movie_id",
    right_on="id"
)

# Count the number of genres
genre_count = genres_movies.groupby("genre").agg({"id": "count"})

# Plot a bar chart of the genre_count
genre_count.plot(kind="bar")
plt.show()

# ============================================
# 4. Additional Notes
# Popular genres with right join
# A right join ensures that ALL popular movies (pop_movies) are kept,
# even if some do not appear in movie_to_genres. This avoids losing
# movies that might be missing genre information.
#
# Steps:
# 1) Merge movie_to_genres ⨝(right) pop_movies using movie_id ↔ id.
# 2) Group by "genre" and count how many popular movies fall into each.
# 3) Plot the counts to visualize genre distribution among top movies.
#
# Context:
# - pop_movies contains the top 10 most popular movies.
# - movie_to_genres contains movie–genre associations.
# - pandas is imported as pd.
# - matplotlib.pyplot is imported as plt.
# ============================================
