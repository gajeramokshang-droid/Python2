import pandas as pd
data={
    "Department":["IT","IT","HR","HR","Finance","IT"],
    "Employee":["A","B","C",'D','E','F'],
    "Salary":[50000,60000,45000,48000,70000,55000],
    "Experience":[2,3,1,2,5,4]
}

df=pd.DataFrame(data)
print(df)

df1=df.groupby(["Department"],as_index=True).sum()
print(df1)

