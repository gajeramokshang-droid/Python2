import pandas as pd

data = {"x1": [1,2,3], "x2": [4,5,6]}
df = pd.DataFrame(data, index=["Mok","Rit","Gaj"])
print(df)
