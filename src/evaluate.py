import pandas as pd

# Load the synthetic dataset
df = pd.read_csv("../data/synthetic_domains.csv")

def score_domain(domain):
    score = 0
    # Score rule: good length
    if len(domain) < 20:
        score += 0.5
    # Score rule: good TLD
    if domain.endswith((".com", ".net", ".org")):
        score += 0.5
    return score

# Apply scoring
df["score"] = df["domain_name"].apply(score_domain)

# Save results
df.to_csv("../data/evaluation_results.csv", index=False)

print("✅ Evaluation done → Saved to data/evaluation_results.csv")
