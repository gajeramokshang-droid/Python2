# Perform outer merge using indicator=True.
import pandas as pd
students = pd.DataFrame({
"ID":[1,2,3,4],
"Name":["A","B","C","D"]
})
marks = pd.DataFrame({
"ID":[2,3,5],
"Score":[85,90,75]
})

jesus=pd.merge(students,marks,on="ID",how='outer',indicator=True)
print(jesus)