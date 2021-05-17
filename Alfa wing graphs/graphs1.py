import pandas as pd

df = pd.read_excel(r'Path where the Excel file is stored\File name.xlsx', sheet_name='your Excel sheet name')
print (df)
