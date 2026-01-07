import pandas as pd
import random


def generate_mock_csv(filename: str = "social_media_data.csv"):
    categories = ["Health", "Family", "Food", "Tech", "Fitness", "Beauty"]
    data = []

    for i in range(100):
        cat = random.choice(categories)
        data.append(
            {
                "Tweet_ID": 1000 + i,
                "Category": cat,
                "Content": f"Amazing post about {cat}! Check this out #trending",
                "Engagement_Score": random.randint(10, 1000),
            }
        )

    pd.DataFrame(data).to_csv(filename, index=False)
    print(f"File {filename} created successfully.")


if __name__ == "__main__":
    generate_mock_csv()
