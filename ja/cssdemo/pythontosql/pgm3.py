from cssdemo.pythontosql.prgm1 import *
db=getconnection()
print(db)
cursor=db.cursor()
try:
    cursor.execute("select * FROM EMPLOYEES")
    myres = cursor.fetchall()
    for x in myres:
        print(x)
except exception as e:
    print(e.arg)
finally:
    db.close()
