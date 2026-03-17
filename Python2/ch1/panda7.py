#create dataframe using dictionary
import pandas as pd
data={"Name":["A","B","C"],"Marks":[85,90,65],"City":["Ahm","Delhi","Bombay"]}
print(pd.Series(data))
print("---------------------")
df=pd.DataFrame(data,index=[1,2,3])
print(df)
