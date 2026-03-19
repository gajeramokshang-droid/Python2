# Detect outliers using IQR method.
# Remove outliers.
# Print cleaned dataset

import pandas as pd
df = pd.DataFrame({
"Salary":[20000,22000,21000,25000,24000,300000]
})

Q1=df["Salary"].quantile(0.25)
Q3=df["Salary"].quantile(0.75)
print(Q1,Q3)

IQR=Q3-Q1
print(IQR)

Low=Q3-(1.5*IQR)
High=Q1+(1.5*IQR)
jesus=df[(df["Salary"]>=Low)|(df["Salary"]<=High)]
print(jesus)