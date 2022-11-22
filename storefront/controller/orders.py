import pandas as pd


def readData():
    data_excel_file = 'storefront\SampleData.xlsx'
    return pd.read_excel(data_excel_file)

df = readData()
print(type(df['OrderDate']))
df['Datetime'] = pd.to_datetime(df['OrderDate'])
print(type(df['Datetime']))
# df.info()clear
df = df.set_index(['Datetime'])
# print(df.head())
# df1 = df[df['Datetime']>'2021-04-01']
df1 = df[df.index.to_series().between('2021-04-01','2022-01-01')]

print(df1)