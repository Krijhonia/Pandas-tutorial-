#fillna()
#fillna(value,inplace=True)
import pandas as pd

data = {
    "Name":['Ram',None,'Dhansyam','Aditi','Jagdish','Raj','Simran','Aman'],
    "Age":[28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance_score":[85,None,89,78,88,92,90,88]
}

df = pd.DataFrame(data)
print(df)

print("Dataframe after using the fillna method")
# df.fillna(0,inplace=True)
df['Age'].fillna(df['Age'].mean(),inplace =True)
df['Salary'].fillna(df['Salary'].mean(),inplace =True)

print(df)
