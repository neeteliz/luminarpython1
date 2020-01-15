import re
str=input("enter the string")
x='^KL[0-9]{2}[A-Z]{2}[0-9]{4}'
match=re.fullmatch(x,str)
if(match!=None):
    print("valid")
else:
    print("invalid")
