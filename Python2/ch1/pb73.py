# Group by Dept.
# Calculate mean, median, and max salary using agg().

import pandas as pd
df = pd.DataFrame({
"Dept":["IT","IT","HR","HR","Finance","Finance"],
"Salary":[50000,70000,40000,60000,80000,75000]
})

jesus=df.groupby(["Dept"]).agg(['min','max','median'])
print(jesus)