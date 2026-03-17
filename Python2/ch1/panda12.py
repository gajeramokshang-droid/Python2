# drop using multiindex

import pandas as pd

# Two arrays (lists)
countries = ["USA", "USA", "India", "India"]
cities    = ["NYC", "LA", "Delhi", "Mumbai"]

# Create MultiIndex
multi_index = pd.MultiIndex.from_arrays([countries, cities], names=["Country", "City"])
print(multi_index)
# Use it in a DataFrame
df = pd.DataFrame({"Population": [8.4, 4.0, 18.9, 12.5]}, index=multi_index)

print(df)
