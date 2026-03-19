# Find number of unique cities per department.
# Take one random employee per department.
# Display results.

import pandas as pd
df = pd.DataFrame({
"Dept":["IT","IT","HR","HR","Finance","Finance"],
"Employee":["A","B","C","D","E","F"],
"City":["X","X","Y","Z","X","Y"]
})

jesus = df.groupby("Dept")["City"].nunique()
print(jesus)


jesus1 = df.groupby("Dept").apply(lambda x: x.sample(1)).reset_index(drop=True)
print(jesus1)
