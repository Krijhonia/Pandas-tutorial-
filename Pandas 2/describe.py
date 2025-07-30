#step-1 making the sample data frame using dictionary

import pandas as pd
data = {
    "Name":['Ram','Shyam','Dhansyam','Aditi','Jagdish','Raj','Simran','Aman'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance score":[85,90,89,78,88,92,90,88]
}
df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)
print('Descriptive stastistics')
print(df.describe())