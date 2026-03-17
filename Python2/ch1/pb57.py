import pandas as pd
import numpy as np
data={"name":['William','Emma','Sofia','Markus','Edward','Thomas','Ethan',np.nan,'Arun','Anika','Paulo'],
      "region": [np.nan, "North", "East", np.nan, "West", "West",'South', np.nan, "West", "East", "South"],
    "sales": [50000.0, 52000.0, np.nan, np.nan, 42000.0, 72000,49000,np.nan,67000, 65000.0, 67000.0],
    "expenses": [42000.0, 43000.0, np.nan, np.nan,38000, 39000.0, 42000, np.nan, 39000, 50000.0, 45000.0]
}
df=pd.DataFrame(data)
print(df)

x1=df.dropna(axis=1)
print(x1)

# x2=df.drop("region",axis=1)
# print(x2)