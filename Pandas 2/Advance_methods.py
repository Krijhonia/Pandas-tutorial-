# Advance methods that are used in pandas in python
import pandas as pd

# Use the provided DataFrame for demonstration

data = {
    "Name":['Ram','Shyam','Dhansyam','Aditi','Jagdish','Raj','Simran','Aman'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance_score":[85,90,89,78,88,92,90,88]
}
df = pd.DataFrame(data)
print('Original DataFrame:')
print(df)

# 1. groupby(): Grouping data and applying functions
print('\nGroup by Performance_score and mean:')
print(df.groupby('Performance_score').mean(numeric_only=True))

# 2. pivot_table(): Creating pivot tables
print('\nPivot table (mean Salary by Performance_score):')
print(df.pivot_table(values='Salary', index='Performance_score', aggfunc='mean'))

# 3. apply(): Apply a function along an axis
print('\nApply function to Age (add 1):')
df['Age_plus_1'] = df['Age'].apply(lambda x: x+1)
print(df)

# 4. map(): Map values of a Series
print('\nMap values in Name:')
df['Name_length'] = df['Name'].map(len)
print(df)

# 5. melt(): Unpivot a DataFrame
print('\nMelt DataFrame:')
melted = pd.melt(df, id_vars=['Name'])
print(melted)

# 6. merge(): Merge two DataFrames
print('\nMerge DataFrames:')
df2 = pd.DataFrame({'Name': ['Ram', 'Aditi'], 'Bonus': [5000, 7000]})
merged = pd.merge(df, df2, on='Name', how='left')
print(merged)

# 7. concat(): Concatenate DataFrames
print('\nConcatenate DataFrames:')
df3 = pd.DataFrame({"Name":['NewEmp'], "Age":[27], "Salary":[55000], "Performance_score":[80]})
concatenated = pd.concat([df, df3], ignore_index=True)
print(concatenated)

# 8. drop_duplicates(): Remove duplicate rows
print('\nDrop duplicates:')
df_dup = pd.concat([df, df.iloc[[0]]], ignore_index=True)
print(df_dup.drop_duplicates())

# 9. fillna(): Fill missing values
print('\nFill missing values:')
df_nan = df.copy()
df_nan.loc[0, 'Salary'] = None
print(df_nan.fillna(0))

# 10. sort_values(): Sort by values
print('\nSort by Salary descending:')
print(df.sort_values('Salary', ascending=False))

# 11. set_index() and reset_index(): Set/reset DataFrame index
print('\nSet and reset index:')
df_indexed = df.set_index('Name')
print(df_indexed)
print(df_indexed.reset_index())

# 12. value_counts(): Count unique values in a column
print('\nValue counts for Performance_score:')
print(df['Performance_score'].value_counts())

# 13. nunique(): Number of unique values in each column
print('\nNumber of unique values in each column:')
print(df.nunique())

# 14. isin(): Filter rows by values
print('\nRows where Name is Ram or Aditi:')
print(df[df['Name'].isin(['Ram', 'Aditi'])])

# 15. query(): Query DataFrame with a string expression
print('\nQuery DataFrame:')
print(df.query('Age > 30 and Salary < 70000'))

# These are some of the most commonly used advanced DataFrame methods in pandas.
