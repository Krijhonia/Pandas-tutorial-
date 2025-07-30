#head()
#tail()
import pandas as pd
df = pd.read_json("sample_Data.json")

print('Display ten row of first')
print(df.head(10))

print('Display ten rows of last')
print(df.tail(10))