#Concat  sort 
import pandas as pd
df1=pd.DataFrame({"C":[1,2],"B":[2,3]})
df2=pd.DataFrame({"A":[5,6],"B":[7,8]})
result=pd.concat([df2,df1],sort=True,ignore_index=True) 
print(result)
