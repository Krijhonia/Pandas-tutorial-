# Import the pandas library for data manipulation
import pandas as pd

# Create a dictionary with sample data
data = {
    "Name":['Ram','Shyam','Dhansyam','Aditi','Jagdish','Raj','Simran','Aman'],  # List of names
    "Age":[28,34,22,30,29,40,25,32],  # List of ages
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],  # List of salaries
    "Performance score":[85,90,89,78,88,92,90,88]  # List of performance scores
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display a message before printing the DataFrame
print("Sample dataframe")
# Print the entire DataFrame
print(df)
# Display a message before printing the 'Name' column
print("Names (Single columns return series)")
# Print the 'Name' column (returns a Series)
print(df["Name"])

#Selecting multiple columns
subset = df[["Name","Salary"]]
print('\nSubset with Name and Salary')
print(subset)