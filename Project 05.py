# ============================================
# 1. Task Description
# Perform a hypothesis test to determine whether the mean number of goals
# scored in women’s international soccer matches differs from that of men’s,
# using Official FIFA World Cup matches since 2002-01-01 and assuming
# independence across matches. Because goals are count data and typically
# non-normal, apply a non-parametric Wilcoxon–Mann–Whitney test.
# Store the p-value and the decision ("reject" / "fail to reject") at
# a 10% significance level in:
#     result_dict = {"p_val": p_val, "result": result}
#
# 2. Topics Covered
# - Data filtering by date and competition
# - Constructing a per-match goals metric
# - Non-parametric two-sample testing (Mann–Whitney U)
# - One dictionary output with p-value and decision
# ============================================

# 3. Python Script

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import pingouin
from scipy.stats import mannwhitneyu

# Load men's and women's datasets
men = pd.read_csv("men_results.csv")
women = pd.read_csv("women_results.csv")

# Filter the data for the time range and tournament
men["date"] = pd.to_datetime(men["date"])
men_subset = men[(men["date"] > "2002-01-01") & (men["tournament"].isin(["FIFA World Cup"]))]
women["date"] = pd.to_datetime(women["date"])
women_subset = women[(women["date"] > "2002-01-01") & (women["tournament"].isin(["FIFA World Cup"]))]

# Create group and goals_scored columns
men_subset["group"] = "men"
women_subset["group"] = "women"
men_subset["goals_scored"] = men_subset["home_score"] + men_subset["away_score"]
women_subset["goals_scored"] = women_subset["home_score"] + women_subset["away_score"]

# Determine normality using histograms
men_subset["goals_scored"].hist()
plt.show()
plt.clf()

# Goals scored is not normally distributed, so use Wilcoxon-Mann-Whitney test of two groups
women_subset["goals_scored"].hist()
plt.show()
plt.clf()

# Combine women's and men's data and calculate goals scored in each match
both = pd.concat([women_subset, men_subset], axis=0, ignore_index=True)

# Transform the data for the pingouin Mann-Whitney U t-test/Wilcoxon-Mann-Whitney test
both_subset = both[["goals_scored", "group"]]
both_subset_wide = both_subset.pivot(columns="group", values="goals_scored")

# Perform right-tailed Wilcoxon-Mann-Whitney test with pingouin
results_pg = pingouin.mwu(x=both_subset_wide["women"],
                          y=both_subset_wide["men"],
                          alternative="greater")

# Alternative SciPy solution: Perform right-tailed Wilcoxon-Mann-Whitney test with scipy
results_scipy = mannwhitneyu(x=women_subset["goals_scored"],
                             y=men_subset["goals_scored"],
                             alternative="greater")

# Extract p-value as a float
p_val = results_pg["p-val"].values[0]

# Determine hypothesis test result using sig. level
if p_val <= 0.1:
    result = "reject"
else:
    result = "fail to reject"

result_dict = {"p_val": p_val, "result": result}

# ============================================
# 4. Additional Notes
# Hypotheses (two-sided):
# - H0: The distributions (and, in many interpretations, central tendencies)
#       of goals per match are the same for men’s and women’s World Cups.
# - H1: They differ.
#
# Rationale:
# - Goals per match are integer counts with skew and limited support. The
#   Wilcoxon–Mann–Whitney (rank-sum) test is robust to non-normality and
#   compares central tendencies via ranks.
#
# Assumptions:
# - Independence of matches (team-form/serial effects ignored, as specified).
# - Ordinal/continuous response (goals are discrete counts but acceptable for WMW).
# - Two-sided alternative since we are testing for any difference, not direction.
#
# Output:
# - result_dict contains the p-value (float) and the decision string using α = 0.10.
# ============================================
