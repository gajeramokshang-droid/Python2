#Concat
import pandas as pd
df1=pd.DataFrame({"A":[1,2],"B":[2,3]})
df2=pd.DataFrame({"A":[5,6],"B":[7,8]})
result=pd.concat([df1,df2])
print(result)