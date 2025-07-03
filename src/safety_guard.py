
import pandas as pd

# Test business descriptions
requests = [
    "organic coffee shop downtown",
    "vegan bakery",
    "adult content website with explicit nude content",
    "family-friendly pet grooming service"
]

def is_safe(description):
    # Example banned words
    banned = ["adult", "explicit", "nude", "xxx", "porn"]
    desc = description.lower()
    for word in banned:
        if word in desc:
            return "blocked"
    return "allowed"

# Build results
data = []
for req in requests:
    status = is_safe(req)
    data.append({"business_description": req, "status": status})

df = pd.DataFrame(data)
df.to_csv("../data/safety_test.csv", index=False)

print("✅ Safety guard test done → Results saved to data/safety_test.csv")
