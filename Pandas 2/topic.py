"""
1. How big is your data set
2. What are the names of the columns

there are two attributes in pandas named 
as shape and column in python for this 
"""

import pandas as pd
data = {
    "Name":['Ram','Shyam','Dhansyam','Aditi','Jagdish','Raj','Simran','Aman'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance score":[85,90,89,78,88,92,90,88]
}

df = pd.DataFrame(data)
print(f'Shape: {df.shape}')
print(f'Column names: {df.columns}')
print(df)