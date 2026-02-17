import pandas as pd


data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Sara", "Ahmed", "John", "Maria", "Ali"],
    "Role": ["AI Engineer", "Data Analyst", "ML Ops", "AI Engineer", "Data Analyst"],
    "Salary": [95000, 72000, 88000, 105000, 65000],
    "Experience (Yrs)": [3, 1, 5, 4, 2]
}

df_employees = pd.DataFrame(data)

print("===== Original DataFrame =====")
print(df_employees)
print()


#  Filtering
filtered_df = df_employees[
    (df_employees["Role"] == "AI Engineer") &
    (df_employees["Experience (Yrs)"] > 3)
]

print("===== Filtered Data (AI Engineers with >3 years experience) =====")
print(filtered_df)
print()


# Aggregation
avg_salary = df_employees.groupby("Role")["Salary"].mean()

print("===== Average Salary Grouped by Role =====")
print(avg_salary)
print()


# Add Conditional Column 
df_employees["Level"] = df_employees["Experience (Yrs)"].apply(
    lambda x: "Senior" if x >= 4 else "Junior"
)

print("===== DataFrame After Adding 'Level' Column =====")
print(df_employees)
