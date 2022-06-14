s=1124342355
c=0
l=[]
while s>0:
    m=s%10
    l.append(m)
    s=s//10
for i in l:
    if l.count(i)==1:
        c+=1
print(l)
print(c)
