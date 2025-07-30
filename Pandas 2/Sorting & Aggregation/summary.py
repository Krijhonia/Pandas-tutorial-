#It gives the summary of the stastics
# df['Column name'].mean()
import pandas as pd
data={
    "Name" : ['Varun','Arun','Karun'],
    "Age": [28,34,22],
    "Salary" : [10000,20000,30000]
}

df = pd.DataFrame(data)
print(df)
avg_salary = df['Salary'].mean()
print(avg_salary)