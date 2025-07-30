# dropna()
#If we set the axis = 0 then it means we are deleting the rows 
#If we are setting axis = 1 then it means we are deleting the columns
import pandas as pd

data = {
    "Name":['Ram',None,'Dhansyam','Aditi','Jagdish','Raj','Simran','Aman'],
    "Age":[28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance_score":[85,None,89,78,88,92,90,88]
}

df = pd.DataFrame(data)
print(df)

# df.dropna(axis = 0, inplace=True)

df.dropna(inplace = True)
print(df)