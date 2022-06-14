'''
d={104:"Suraj",101:"Ram",100:"Dinesh"}
s=sorted([(key,value) for (key,value)in d.items()])
print(s)

import operator
d={104:"Suraj",101:"Ram",100:"Dinesh"}
print(d)
z=sorted(d.items(),key=operator.itemgetter(1))
print(z)
y=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print(y)
print(d[100])

d[104]="Nikhil"
print(d)
del d[100]
print(d)
d[103]='Nilam'
print(d)
for k in d:
    print(k,end=':')
    print(d[k],end=',')
print(d.keys())
print(d.values())
print(d.items())


s="suraj","ram","shyam","ramu",'sam','dam'
d={e:s[e] for e in range(1,len(s))}
print(d,end=' ')
    
d={104:"Suraj",101:"Ram",100:"Dinesh"}
for k,v in d.items():
    print([v,k])

d={104:"Suraj",101:"Ram",100:"Dinesh"}
for k,v in d.items():
    print(v,k)
'''
#number as a key square of that number as a values
d={l:l**2 for l in range(1,10)}
print(d)

