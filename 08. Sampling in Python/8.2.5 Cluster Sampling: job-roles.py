# ============================================
# 1. Task Description
# Perform cluster sampling on the attrition dataset by:
# 1) Randomly selecting a subset of job roles (clusters),
# 2) Filtering the population to only those clusters,
# 3) Drawing an equal number of employees from each selected job role.
#
# 2. Topics Covered
# - Cluster sampling workflow
# - Random sampling of categorical levels
# - Filtering with .isin() and removing unused categories
# - Stratified sampling within selected clusters
# ============================================

# 3. Python Script

# Create a list of unique JobRole values
job_roles_pop = list(attrition_pop["JobRole"].unique())

# Randomly sample four JobRole values
job_roles_samp = random.sample(job_roles_pop, k=4)

# Filter for rows where JobRole is in job_roles_samp
jobrole_condition = attrition_pop["JobRole"].isin(job_roles_samp)
attrition_filtered = attrition_pop[jobrole_condition]

# Remove categories with no rows
attrition_filtered["JobRole"] = attrition_filtered["JobRole"].cat.remove_unused_categories()

# Randomly sample 10 employees from each sampled job role
attrition_clust = (
    attrition_filtered.groupby("JobRole")
    .sample(n=10, random_state=2022)
)

# Print the sample
print(attrition_clust)

# ============================================
# 4. Additional Notes
# Performing cluster sampling
# - Treat each JobRole as a cluster. First, select a handful of clusters
#   (here, 4) at random, then sample a fixed number of observations from
#   each chosen cluster (here, 10 employees per role).
# - This differs from stratified sampling where *all* clusters (strata)
#   are represented; in cluster sampling, only a subset of clusters is used.
# - Removing unused categories keeps categorical dtype tidy after filtering.
#
# Tips:
# - Ensure `random.seed(19790801)` (as provided) to make the job role
#   selection reproducible if that’s a requirement.
# - If some clusters are too small (< n), replace `n=` with `frac=`
#   or add safeguards to handle undersized clusters.
#
# Context:
# pandas is loaded as pd, and `attrition_pop` is available.
# The standard library `random` is available and seeded externally.
# ============================================
