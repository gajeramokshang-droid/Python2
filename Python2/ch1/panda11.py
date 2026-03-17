import pandas as pd

data = {"RollNo":[101,102,103,104],
        "Name":["A","B","C","D"],
        "Marks":[85,95,63,70],
        "Age":[20,21,19,22]}
df = pd.DataFrame(data)
print(df)
c1=df.loc[3]=[105,'F',12,3]
print(c1)
print(df)

c2=df.iloc[2,3]=100
print(c2)
print(df)

cd=df.info()
print("info=",cd)

cd1=df.describe()
print("Describe",cd1)
