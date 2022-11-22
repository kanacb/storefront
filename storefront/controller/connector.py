# pip install mysql.connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE storefront")