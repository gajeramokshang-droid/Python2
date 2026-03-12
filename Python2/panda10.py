# Read CSV FILE
import pandas as pd
df=pd.read_csv("auto-mpg.csv")
print(df)
print("------Head------")
print(df.head())
print(df.head(8))

print("-----------Tail-----------")
print(df.tail())
print(df.tail(8))

print("--------------loc------------")
print(df.loc[11:18])

print("-------------iloc--------------")
print(df.iloc[11:18,0:3:2])
print(df.iloc[1:21:2,3:4:1])
print(df.iloc[1:4,3:4:1])

print("------------------------")
print(df['mpg'])
print(df[['mpg']])

print("==================================")
print(df[['mpg','cylinders','displacement','horsepower']].loc[21:30] )

print("====================================")
print(df[["model year","car name"]].loc[49:33:-4])


print('===================================')
print(df[df['cylinders']==4])

print('===================================')
print(df[(df['weight']>=3400) & (df['weight']<=3600)])


print('========================')
print(df.shape)

print(type(df.shape))

print(df.columns)
print(df['mpg'].rolling)
print("----------------")
print(df['mpg'].rolling(window=3).mean())
print(df['cylinders'].rolling(window=3).mean)

print("============= SET INDEX ======================")
data = {"RollNo":[101,102,103],
         "Name":["A","B","C"],
         "Marks":[85,95,63]}

df=pd.DataFrame(data)
print("df=",df)
v1=df.set_index("RollNo")
print(v1)
v2=df.set_index("RollNo",drop=False)
print(v2)


print("==========inplace===========")
v4=df.set_index("RollNo",inplace=True)
print(v4)
print(df)

