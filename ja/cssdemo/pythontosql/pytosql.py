import mysql.connector
db =mysql.connector.connect(
    host="localhost",
    user="root",
    password="password@123"
)

cursor=db.cursor()
cursor.execute("select version()")

data=cursor.fetchone()
print("dataversion:%s"%data)
db.close