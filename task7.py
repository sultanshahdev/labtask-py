import pandas as pd


data = {
    "Project_ID": [201, 202, 203, 204, 205, 206],
    "Student_Name": ["Zara", "Hassan", "Ayesha", "Bilal", "Noor", "Taha"],
    "Domain": ["Vision", "NLP", "Robotics", "Vision", "NLP", "Vision"],
    "Score": [88, 76, 91, 83, 69, 95],
    "Days_Late": [1, 0, 2, 0, 3, 0]
}

df = pd.DataFrame(data)

print("===== Original DataFrame =====")
print(df)
print()


# 1️⃣ Grouping: Average score for each Domain
avg_scores = df.groupby("Domain")["Score"].mean()

print("===== Average Score per Domain =====")
print(avg_scores)
print()


#Counting: Number of projects per Domain
project_counts = df["Domain"].value_counts()

print("===== Project Count per Domain =====")
print(project_counts)
print()


# Sorting:
# Sort by Days_Late (ascending) then by Score (descending)
sorted_df = df.sort_values(
    by=["Days_Late", "Score"],
    ascending=[True, False]
)

print("===== Sorted DataFrame =====")
print(sorted_df)
