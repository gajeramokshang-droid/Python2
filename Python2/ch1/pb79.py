# Find the number of employees per department using size().
# Find the employee with highest experience in each department using nth() or sorting.
# Display results

import pandas as pd
df = pd.DataFrame({
"Dept":["IT","IT","HR","HR","Finance","Finance"],
"Employee":["A","B","C","D","E","F"],
"Experience":[2,5,3,7,4,6]
})
noofemp=df.groupby("Dept").size()
print(noofemp)

# noofemp1=df.sort_values(by=["Dept","Experience"],ascending=[True,False]).groupby("Dept").head(1)
# print(noofemp1)


jesus=df.groupby("Dept")["Experience"].nth(1)
print(jesus)
