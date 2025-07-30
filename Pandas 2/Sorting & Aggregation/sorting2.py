import pandas as pd
data={
    "Name" : ['Varun','Arun','Karun'],
    "Age": [28,34,22],
    "Salary" : [10000,20000,30000]
}

df = pd.DataFrame(data)
print(df)
df.sort_values(by=["Age","Salary"], ascending=[True,False], inplace=True)
print('Sorted age by descending')
print(df)