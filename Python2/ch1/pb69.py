# Create a column Average using apply() row-wise.
# Create a column Grade based on:
# ≥ 80 → Dis􀆟nc􀆟on
# ≥ 60 → First
# Otherwise → Second
# Display final DataFrame.
# apply() in pandas is simply used to run a function on your DataFrame or Series.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Student":["A","B","C","D"],
    "Math":[70,45,90,60],
    "Science":[75,40,85,55]
})

print(df)
df["Average"] = df[["Math","Science"]].apply(np.mean,axis=1) 
print(df)
def grade(avg):
    if(avg>80):
        return "Dist"
    elif(avg>60):
        return "Firts"
    else:
        return "second"

df["Grade"]=df["Average"].apply(grade)
print(df)

