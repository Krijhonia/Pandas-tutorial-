# Removing columns in pandas 
import pandas as pd

data = {
    "Name":['Ram','Shyam','Dhansyam','Aditi','Jagdish','Raj','Simran','Aman'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance_score":[85,90,89,78,88,92,90,88]
}

df = pd.DataFrame(data)
print(df)

# df.drop(columns = ["Column_name"], inplace = True)
# True condition is used to modify the original dataframe
#If you use the false condition then it will create the copy of the dataframe

df.drop(columns=["Performance_score"],inplace=True)
print("Dataframe without the performance score column")
print(df)

df.drop(columns=["Age"],inplace=True)
print("Dataframe without the Age and performance score column")
print(df)

#Always use the true condition to modify the original dataframe
