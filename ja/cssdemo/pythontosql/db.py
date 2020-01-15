from cssdemo.pythontosql.prgm1 import *
db=getconnection()
print(db)
cursor=db.cursor()
cursor.execute("drop table if exist employee")

sql="""CREATE TABLE EMPLOYEE(
     FIRST NAME CHAR(20),
     LAST NAME CHAR(20),
     AGE INT(2),
     SEX CHAR(20),
     INCOMEFLOAT(),"""
cursor.execute(sql)
db.close()


