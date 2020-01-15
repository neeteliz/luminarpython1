import re
mobile=input("enter the mobile no:")
x='^91[0-9]{10}'
matcher=re.fullmatch(x,mobile)
if(matcher!=None):
    print("valid")
else:
    print("invalid")