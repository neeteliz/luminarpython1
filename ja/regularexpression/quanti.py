import re
str=input("enter the string")
x='[a-k][3,6,9][A-Za-z0-9]*'
match=re.fullmatch(x,str)
if(match!=None):
    print("valid")
else:
    print("invalid")
