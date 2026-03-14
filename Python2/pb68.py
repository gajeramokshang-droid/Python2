# Sort employees by Dept (Ascending) and Salary (Descending).
# After sorting, sort the index in descending order.
# Display the final DataFrame.
import pandas as pd
data = {
"EmpID":[101,102,103,104,105],
"Dept":["IT","HR","IT","Finance","HR"],
"Salary":[60000,45000,80000,75000,50000],
"Age":[25,32,29,41,28]
}
df = pd.DataFrame(data)
print(df)

c1=df.sort_values(by=["Dept","Salary"],ascending=[True,False])
print("Sort Dept and Salary=====",c1)

c2=c1.sort_index(ascending=False)
print(c2)