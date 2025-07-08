import pandas as pd
from collections import Counter
import os

# Load the scraped jobs data
df = pd.read_csv("data/jobs.csv")

# Prepare skill list
all_skills = []

for skills_str in df["Skills"].dropna():
    skills = [skill.strip().lower() for skill in skills_str.split(",")]
    all_skills.extend(skills)

# Count frequency
skill_counts = Counter(all_skills)

# Show top 20 skills
print("🔥 Top 20 Skills:")
for skill, count in skill_counts.most_common(20):
    print(f"{skill}: {count}")

# Optional: Save to CSV
skill_df = pd.DataFrame(skill_counts.items(), columns=["Skill", "Count"]).sort_values(by="Count", ascending=False)
skill_df.to_csv("data/skill_trends.csv", index=False)

print("\n✅ Skill trend data saved to data/skill_trends.csv")
