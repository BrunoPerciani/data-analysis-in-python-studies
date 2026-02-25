# ============================================
# 1. Task Description
# Concatenate multiple DataFrames containing track information from
# different Metallica albums into a single table. The goal is to perform
# a vertical concatenation while keeping only columns shared by all
# DataFrames.
#
# 2. Topics Covered
# - Vertical concatenation with pd.concat()
# - Using join="inner" to keep only common columns
# - Handling multiple DataFrames at once
# - Inspecting the resulting concatenated output
# ============================================

# 3. Python Script

# Concatenate the tracks, show only column names that are in all tables
tracks_from_albums = pd.concat(
    [tracks_master, tracks_ride, tracks_st],
    join="inner",
    sort=True
)
print(tracks_from_albums)

# ============================================
# 4. Additional Notes
# Concatenation basics
# pd.concat() is used to stack DataFrames either vertically (axis=0) or
# horizontally (axis=1). Here, vertical concatenation is used so that
# tracks from different albums appear as additional rows.
#
# - join="inner" keeps only the columns that all DataFrames share.
# - sort=True sorts the columns alphabetically in the output.
#
# Context:
# The DataFrames `tracks_master`, `tracks_ride`, and `tracks_st` contain
# track info from Metallica’s Master of Puppets, Ride the Lightning, and
# St. Anger albums. pandas is imported as pd.
# ============================================
