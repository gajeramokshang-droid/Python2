import pandas as pd
import numpy as np
data={"name":['William','Emma','Sofia','Markus','Edward','Thomas','Ethan',np.nan,'Arun','Anika','Paulo'],
      "region": [np.nan, "North", "East", np.nan, "West", "West",'South', np.nan, "West", "East", "South"],
    "sales": [50000.0, 52000.0, np.nan, np.nan, 42000.0, 72000,49000,np.nan,67000, 65000.0, 67000.0],
    "expenses": [42000.0, 43000.0, np.nan, np.nan,38000, 39000.0, 42000, np.nan, 39000, 50000.0, 45000.0]
}
df=pd.DataFrame(data)
print(df)

Q1=df['sales'].quantile(0.25)
Q3=df['expenses'].quantile(0.75)
IQR=Q3-Q1
print(IQR)
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
print(lower_bound)
print(upper_bound)
jesus=df[(df['sales']>lower_bound)|(df['expenses']<upper_bound)]
print(jesus)
