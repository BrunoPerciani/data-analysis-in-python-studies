# ============================================
# 1. Task Description
# Identify science fiction movies that are NOT also classified as action
# by leveraging a right join between action_movies and scifi_movies, then
# filter rows where the action genre is missing. Finally, merge with the
# movies table to retrieve movie names and basic metadata.
#
# 2. Topics Covered
# - Right joins with .merge(how="right")
# - Filtering nulls to find "only-in-right-table" records
# - Inner joining to enrich the filtered set with movie details
# - Inspecting results (preview and shape)
# ============================================

# 3. Python Script

# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(
    scifi_movies,
    on="movie_id",
    how="right",
    suffixes=("_act", "_sci")
)

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi["genre_act"].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(
    scifi_only,
    left_on="id",
    right_on="movie_id"
)

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)

# ============================================
# 4. Additional Notes
# Right join to find unique movies
# The right join ensures we keep ALL rows from scifi_movies while matching
# any overlapping entries from action_movies. Rows with a null 'genre_act'
# indicate titles that appear only in scifi_movies (i.e., not action).
#
# Steps:
# - action_movies ⨝(right) scifi_movies on movie_id → keep all sci-fi rows.
# - Filter where 'genre_act' is null → sci-fi only.
# - Inner join with movies on id/movie_id to fetch movie names/metadata.
#
# Context:
# The DataFrames `movies`, `scifi_movies`, and `action_movies` are preloaded.
# pandas is imported as pd.
# ============================================
