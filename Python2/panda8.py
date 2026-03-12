#create dataframe using list 
import pandas as pd
data=[['a',80],['b',90]]
print(pd.DataFrame(data,columns=['name','marks'],index=[1,2]))
