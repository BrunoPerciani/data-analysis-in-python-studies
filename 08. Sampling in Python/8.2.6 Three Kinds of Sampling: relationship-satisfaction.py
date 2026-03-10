# ============================================
# 1. Task Description
# Prepare cluster sampling based on the RelationshipSatisfaction variable
# from the attrition population dataset. Randomly select 2 satisfaction
# levels (clusters), filter the population to those levels, and draw a
# cluster sample equal to 25% of the total population size (len(pop)//4).
# This will later be compared with simple and stratified sampling.
#
# 2. Topics Covered
# - Selecting random clusters from a categorical variable
# - Filtering with .isin() and removing unused categories
# - Cluster sampling with groupby().sample()
# ============================================

# 3. Python Script

# Create a list of unique RelationshipSatisfaction values
satisfaction_unique = list(attrition_pop["RelationshipSatisfaction"].unique())

# Randomly sample 2 unique satisfaction values
satisfaction_samp = random.sample(satisfaction_unique, k=2)

# Filter for satisfaction_samp and clear unused categories from RelationshipSatisfaction
satis_condition = attrition_pop["RelationshipSatisfaction"].isin(satisfaction_samp)
attrition_clust_prep = attrition_pop[satis_condition]
attrition_clust_prep["RelationshipSatisfaction"] = (
    attrition_clust_prep["RelationshipSatisfaction"].cat.remove_unused_categories()
)

# Perform cluster sampling on the selected group, getting 0.25 of attrition_pop
attrition_clust = (
    attrition_clust_prep.groupby("RelationshipSatisfaction")
    .sample(n=len(attrition_pop) // 4, random_state=2022)
)

# (Optional) Quick sanity checks
print("Chosen clusters:", satisfaction_samp)
print("Cluster sample shape:", attrition_clust.shape)
print(attrition_clust["RelationshipSatisfaction"].value_counts())

# ============================================
# 4. Additional Notes
# 3 kinds of sampling
# - Cluster sampling: pick a subset of categories (clusters) first, then
#   sample within only those chosen clusters (done here).
# - Stratified sampling: sample from *all* categories (strata), typically
#   proportionally or with equal counts per stratum.
# - Simple random sampling: pick rows at random from the full population
#   without regard to subgroup structure.
#
# Tips:
# - Ensure `random.seed(...)` was set earlier to reproduce the cluster
#   selection (as noted in the exercise).
# - If any chosen cluster has fewer rows than required for n=len(pop)//4
#   when split across two clusters, consider using `frac=` or adding a
#   fallback to avoid errors.
# ============================================
