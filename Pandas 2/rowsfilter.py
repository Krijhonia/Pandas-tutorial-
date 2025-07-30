import pandas as pd
data = {
    "Name":['Ram','Shyam','Dhansyam','Aditi','Jagdish','Raj','Simran','Aman'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance_score":[85,90,89,78,88,92,90,88]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary']>50000]
print("Employees with salary > 50000")
print(high_salary)

#Filtering rows salary > 50k and age > 30
filtered = df[(df['Age']>30)&(df['Salary']>50000)]
print('Employees list Age > 30 and salary >50000')
print(filtered)

#Using or conditions
filtered_or = df[(df['Age'] > 30) | (df['Salary'] > 50000)]
print('Employees with Age > 30 OR salary > 50000')
print(filtered_or)