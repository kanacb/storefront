import pandas as pd

def readData():
    data_csv_file = 'https://github.com/drriley/grocery/blob/master/lib/items.csv?raw=true'
    return pd.read_csv(data_csv_file)


df = readData()
# print(df.head(10))
dfDairy = df[df['Category'].str.contains('Grain', na=False)]
dfDairySorted = dfDairy.sort_values(by='Generic Name')
print(dfDairySorted.reset_index())

