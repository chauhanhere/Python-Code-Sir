from collections import Counter
#this will find the number of words present in a which i want to find with the counter
a="suraj","is","chau","my","suraj","my","suraj","suraj"
b="suraj"
m=Counter(a)
print("m=",m)
for i in m:
    print(i)#printing elemments
    print("number of",i,"=",m[i])#printing counting of elements
    #print(v)
    if i==b:
        print(m[i])
'''
#Solution of above question without counter function
a="suraj","is","chau","my","suraj","my","suraj","suraj"
b="suraj"
c=0
for i in a:
    if i==b:
        c+=1
print(c)
'''
