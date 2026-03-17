# Replace "Absent" with 0.
# Convert the column to integer type.
# Print mean marks.
# Print number of students scoring above 50.

import pandas as pd
df = pd.DataFrame({
"Marks":["50","60","Absent","70","Absent"]
})
print(df)
df["Marks"]=df["Marks"].replace("Absent", 0)
df["Marks"]=df["Marks"].astype(int)
print(df['Marks'].mean())
print((df["Marks"]>50).count())
