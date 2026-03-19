# Calculate range (max - min) per team using groupby + apply.
import pandas as pd
df = pd.DataFrame({
"Team":["A","A","A","B","B"],
"Runs":[50,70,80,40,60]
})
print(df)

df1=df.groupby("Team")["Runs"].apply(lambda x:x.max()-x.min())
print(df1)

