from math import gcd
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if gcd(a,b)==1:
    print(a,"and ",b," are coprime")
else:
    print(a,"and ",b," are not coprime")



#calling is_prime function and passing two arguments will give you result 
    
#def gcd(p,q):
#    while q != 0:
#        p, q = q, p%q
#    return p
#def is_coprime(x, y):
#    return gcd(x, y) == 1
