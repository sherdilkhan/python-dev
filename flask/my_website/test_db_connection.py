import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ns2b78MYS@",
  database="my_website"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user_data")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)