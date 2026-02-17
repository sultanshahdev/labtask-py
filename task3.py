import pandas as pd

# Recreate DataFrame (from Task 1)
data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Sara", "Ahmed", "John", "Maria", "Ali"],
    "Role": ["AI Engineer", "Data Analyst", "ML Ops", "AI Engineer", "Data Analyst"],
    "Salary": [95000, 72000, 88000, 105000, 65000],
    "Experience (Yrs)": [3, 1, 5, 4, 2]
}

df = pd.DataFrame(data)

print("===== Original DataFrame =====")
print(df)
print()


# 1. Introduce a None value into the Salary column
df.loc[2, "Salary"] = None   # Setting John's salary to None

print("===== After Introducing Missing Value =====")
print(df)
print()


# 2. Fill missing value with median salary of the column
median_salary = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_salary)

print("===== After Filling Missing Value with Median =====")
print(df)
print()


# 3. Sort by Salary in descending order and reset index
df = df.sort_values(by="Salary", ascending=False).reset_index(drop=True)

print("===== Final Sorted DataFrame (Descending Salary) =====")
print(df)
