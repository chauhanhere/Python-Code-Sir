s=input("Enter the string")
i=0
v=""
for x in s:
    if s.index(x)==i:
        v+=x
    i+=1
print(v)
    
