'''
s=(10,104,5,43.0,22)
print(type(s))
x=s[::2]
print(x)
print(len(s))#to count elements in the list
print(max(s),min(s))
b=print(sorted(s))
print(sum(s))
c=print(sorted(s,reverse=True))
print(b+c)

s=(10,104,5,43.0,22)
v=sorted(s)
print("Second largest element=",v[-2])

#merge two sorted tuples
s=(10,104,5,43.0,22)
t=(90,3,12,34,23,76)
x=sorted(s)
y=sorted(t)
print(x+y)

#comparing two tuples
s=tuple(input("Enter the first tuple"))
t=tuple(input("Enter the first tuple"))
print(type(s),type(t))
if(len(s)!=len(t)):
    print("Enter both the tuples of same length")
else:    
    if(s==t):
        print("tuples are same and in the same order")
    else:
        print("No,tuples are not same")

s=(10,20,30)
t=(30,20,20)
x=sorted(s)
y=sorted(t)
if(len(s)!=len(t)):
    print("Enter both the tuples of same length")
if(x==y):
    print("tuples are same")
else:
    print("not same")
  '''
#packing of tuples
a,b,c=l=(10,20,30)
print(a)
print(b)
print(c)
print(l)

#unpacking of tuples
l=(10,20,64,54)
a,b,c,d=l
print(a,b,c,d)

