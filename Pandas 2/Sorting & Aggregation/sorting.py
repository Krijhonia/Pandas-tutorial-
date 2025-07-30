#sorting data
#Sorting data 1 column sort_values()
# df.sort_values(by="Column_name",True/False,inplace= True)
#If you want to print the columns in ascending order then you have to pass True
#Otherwise for descending you have to pass False

import pandas as pd
data={
    "Name" : ['Varun','Arun','Karun'],
    "Age": [28,34,22],
    "Salary" : [10000,20000,30000]
}

df = pd.DataFrame(data)
print(df)
df.sort_values(by="Age", ascending=False, inplace=True)
print('Sorted age by descending')
print(df)