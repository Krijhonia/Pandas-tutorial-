# Import pandas library for data manipulation
import pandas as pd

# Create a dictionary with sample employee data
data = {
    "Name":['Ram','Shyam','Dhansyam','Aditi','Jagdish','Raj','Simran','Aman'],  # List of employee names
    "Age":[28,34,22,30,29,40,25,32],  # List of ages
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],  # List of salaries
    "Performance_score":[85,90,89,78,88,92,90,88]  # List of performance scores
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
# Print the original DataFrame
print(df)

# Increase salary by 5 percent for all employees
# This multiplies each value in the 'Salary' column by 1.05
# and updates the column with the new values
df['Salary'] = df['Salary'] * 1.05
# Print the updated DataFrame
print(df)