# Group employees by Department.
# Calculate total salary and average salary per department.
# Display departments where average salary is greater than 50,000.

import pandas as pd
df = pd.DataFrame({
"Employee":["A","B","C","D","E"],
"Dept":["IT","HR","IT","Finance","HR"],
"Salary":[50000,40000,70000,80000,45000]
})

grpemp=df.groupby("Employee")['Salary'].agg(['sum','mean'])
print(grpemp)

jesus=grpemp[grpemp["mean"]>50000]
print("Deprt sala > than 50k",jesus)