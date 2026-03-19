# Concatenate row-wise using outer join.
# Count total missing values.
# Sort the result by ID.

import pandas as pd
df1 = pd.DataFrame({
"ID":[1,2,3],
"Name":["A","B","C"]
})

df2 = pd.DataFrame({
"ID":[2,3,4],
"Marks":[80,90,70]
})

jesus=pd.concat([df1,df2],join="outer")
print(jesus)


christ=jesus.isnull().sum()
print(christ)

mary=jesus.sort_index()
print(mary)