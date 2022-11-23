import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="storefront",
  password=""
)


mycursor = mydb.cursor()

def readData():
    data_csv_file = 'https://github.com/drriley/grocery/blob/master/lib/items.csv?raw=true'

    return pd.read_csv(data_csv_file)

try:
    df = readData()
    df=df.dropna().reset_index(drop=True)
    print(df.head(10))
    for row in df.iterrows():
        # print(row[1][0],row[1][1],row[1][2],row[1][3])
        statement = "INSERT INTO products (genericName,name,category,location) VALUES(%s,%s,%s,%s)"
        values = (row[1][0],row[1][1],row[1][2],row[1][3])
        mycursor.execute(statement, values)
        
        # mycursor.execute("select * from products where id = ?", 2)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")
except mysql.connector.Error as error :
    mydb.rollback()
    print("Database Update Failed !: {}".format(error))

mydb.close()