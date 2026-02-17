import pandas as pd

# Step 1: Create a new DataFrame manually
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


# Step 2: Apply Penalty Logic
# If Days_Late > 0, subtract 5 points
df["Final_Score"] = df["Score"] - df["Days_Late"].apply(lambda x: 5 if x > 0 else 0)

print("===== After Adding Final_Score =====")
print(df)
print()


# Step 3: Filter Vision projects with Final_Score > 80
filtered_df = df[
    (df["Domain"] == "Vision") &
    (df["Final_Score"] > 80)
]

print("===== Filtered Projects (Vision & Final_Score > 80) =====")
print(filtered_df)
