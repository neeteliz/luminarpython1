import re
x='\w'
matcher=re.finditer(x,'a7b @Ak9z')
for match in matcher:
    print("match available at",match.start())
    print("group",match.group())

