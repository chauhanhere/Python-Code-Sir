n=int(input("Enter the number to print "))
a=0
b=1
#print(a)
#print(b)
for s in range(0,n):
    c=a+b
    a=b
    b=c
    print(c)
