s=input("Enter the string")
v=s.split(' ')
for i in range(len(v)):
    v[i]=v[i].lower()#convert list into lower or uppercase
    x=sorted(v)
print(' '.join(x))
