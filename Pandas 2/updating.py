#Updating values
import pandas as pd

data = {
    "Name":['Ram','Shyam','Dhansyam','Aditi','Jagdish','Raj','Simran','Aman'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance_score":[85,90,89,78,88,92,90,88]
}

df = pd.DataFrame(data)
print(df)
#.loc()
# df.loc[row_index,"Column_name"]= new_value
df.loc[0,"Salary"] = 55000
print(df)
