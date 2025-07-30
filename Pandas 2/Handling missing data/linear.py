#Linear interpolate
import pandas as pd
data ={
    "Time" : [1,2,3,4,5],
    "Value" : [10,None,30,None,50]
  }

df = pd.DataFrame(data)
print('Before interpolation')
print(df)

df['Value'] = df['Value'].interpolate(method="linear")
print('After interpolation')
print(df)

"""
Example usage:
1. Time series data
2. numeric data with trends
3. avoid dropping rows
Disadvantages of interpolation:
1. you cannot work with categorical data
2. It assumes a predictable pattern which always might not exist
"""