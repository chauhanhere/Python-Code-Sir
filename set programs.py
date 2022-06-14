'''
s={10,45,34,23}
print(type(s))
print(s)
'''
s={10,45,34,23}
t={10,23,34,45}
print(s.issubset(t))
print(s.issuperset({34}))
print(s.union(t))#Same element at only one time 
print(s.intersection(t))#print element which exist in both the set 
print(type(s))
print(s)
x=sum(s)
print(x,max(s),min(s),len(s))
s.add(10)#10 will not be added bacause 10 alredy exist in set
#and a set cant have duplicate elements
print(s)
s.add(20)
print(s)
s.add("Suraj")
print(s)
#s.add([76,98]),it is error,because set cant have list as an argument
print(s)
s.add((76,98))
print(s)
s.remove(34)
print(s)
z=s.pop()
print(z)
