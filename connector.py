import mysql.connector as mp
mydb = mp.connect(
  host="localhost",
  user="root",
  password="@Root1234",
  database='car_models'
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
mycursor.execute("SELECT * FROM car_samples")
myresult = mycursor.fetchall()
mycursor.execute("select * from car_samples where Number_plate = 'RJ02CC8232'")
res = mycursor.fetchall()
print(res)
