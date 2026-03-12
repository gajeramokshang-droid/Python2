# (V)Create Series by using Array
import pandas as pd
import numpy as np
A=np.array([5,7,9])
s2=pd.Series(A,index=[1,2,3])
print(s2)