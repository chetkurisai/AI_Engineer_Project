import pandas as pd
import random

# Example business types & keywords
business_types = [
    "Coffee Shop",
    "Yoga Studio",
    "Tech Startup",
    "Pet Grooming",
    "Organic Grocery",
    "Digital Marketing Agency",
    "Handmade Crafts",
    "Online Bookstore",
    "Fitness Trainer",
    "Travel Agency"
]

def generate_domain(business):
    keywords = business.lower().replace(" ", "")
    tlds = [".com", ".net", ".org"]
    return f"{keywords}{random.choice(tlds)}"

def create_dataset(num_samples=20):
    data = []
    for _ in range(num_samples):
        business = random.choice(business_types)
        domain = generate_domain(business)
        data.append({"business_description": business, "domain_name": domain})
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = create_dataset(50)
    df.to_csv("../data/synthetic_domains.csv", index=False)
    print("✅ Synthetic dataset saved to data/synthetic_domains.csv")
