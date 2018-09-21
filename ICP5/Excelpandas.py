# import the pandas
import numpy as np
import pandas as pd


excel_file = 'slr04.xls'

df = pd.read_excel(excel_file, sheet_name=0)

print(df.head(20))


print(df.columns.values)

print(df['X'].values)
print(df['Y'].values)
#X = df['x'].values
#Y = df['y'].values

#print(X)
#print(Y)

#csv_file = 'train.csv'


#csv = pd.read_csv(csv_file, sep=',')
#print(csv.head(8))
