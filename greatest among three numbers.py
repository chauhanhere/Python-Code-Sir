a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter first number"))
if(a<b):
    if(b<c):
        print("the greatest number=",c)
    else:
        print("the greatest number=",b)
if(b<a):
    if(c<a):
        print("the greatest number=",a)
    else:
        print("the greatest number=",c)
        
    
