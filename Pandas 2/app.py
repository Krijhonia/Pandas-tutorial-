import pandas as pd

#Read data from CSV file into a dataframe
# df = pd.read_csv("D:/Pandas 2/sales_data_sample.csv",encoding="latin1")
# df = pd.read_excel(r"D:/Pandas 2/SampleSuperstore.xlsx")
df = pd.read_json("sample_Data.json")
print(df)
#gcsfs for reading the cloud data such as google drive