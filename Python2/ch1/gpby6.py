import pandas as pd
data={
    "Department":["IT","IT","HR","HR","Finance","IT"],
    "Employee":["A","B","C",'D','E','F'],
    "Salary":[50000,60000,45000,48000,70000,55000],
    "Experience":[2,3,1,2,5,4]
}

df=pd.DataFrame(data)
print(df)

df1=df.groupby(["Department"]).nth[0]
print(df1)

# - .nth(n) returns the n‑th row from each group after you’ve grouped your DataFrame.
# - Then .nth(0) means: “From each department group, take the first row (0‑based index).”
# - IT → rows [A, B, F]
# - HR → rows [C, D]
# - Finance → row [E]
# .nth(0) picks:
# - IT → first row = A (50000, 2)
# - HR → first row = C (45000, 1)
# - Finance → first row = E (70000, 5
# Exactly — .nth() itself does not do any sorting.
# - .nth(-1) → the last row in each group
# - .nth(-2) → the second‑to‑last row, and so on.
