# Create a new column TotalAmount = Price × Quantity using apply() row-wise.
# Sort the DataFrame by TotalAmount in descending order.

import pandas as pd
df = pd.DataFrame({
"Product":["P1","P2","P3","P4","P5"],
"Price":[100,200,150,300,250],
"Quantity":[5,2,4,1,3]
})
df["TotalAmount"]=df.apply(lambda x: x.Price*x.Quantity,axis=1)
print(df)

sort=df.sort_values(by='TotalAmount',ascending=False)
print(sort)