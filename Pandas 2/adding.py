import pandas as pd

data = {
    "Name":['Ram','Shyam','Dhansyam','Aditi','Jagdish','Raj','Simran','Aman'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance_score":[85,90,89,78,88,92,90,88]
}

df = pd.DataFrame(data)
print(df)

#Square brackets df["Column_name"] = some_data 
#assignment method but not practical in companies because u can't insert a column in a specific index
df["Bonus"] = df['Salary'] * 0.1
print(df)

#Using insert method()
# df.insert(loc,"Column_name",some_data)
df.insert(0,"Employee ID",[10,20,30,40,50,60,70,80])
print(df)