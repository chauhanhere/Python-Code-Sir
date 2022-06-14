'''
#natural number in reverse order
def firstnatural(n):
    for i in range(n,0,-1):
        print(i,end=' ')

firstnatural(int(input("Enter the number")))
'''
#n natural number
def firstnatural(n):
    for i in range(1,n+1):
        print(i,end=' ')

firstnatural(int(input("Enter the number")))

#square of n natural number in reverse order
def firstnatural(n):
    for i in range(n,0,-1):
        print(i*i,end=' ')

firstnatural(int(input("Enter the number")))

#square of n natural number
def firstnatural(n):
    for i in range(1,n+1):
        print(i*i,end=' ')

firstnatural(int(input("Enter the number")))


#function to print n odd natural number
#n natural number
def firstnatural(n):
    for i in range(1,n+1,2):
        print(i,end=' ')

firstnatural(int(input("Enter the number")))

#function to print n even natural number
def firstnatural(n):
    s=0
    for i in range(0,n+1,2):
        print(i,end=' ')

firstnatural(int(input("Enter the number")))


#function to print sum of n natural numbers
def sumN(n):
    s=0
    for i in range(0,n+1,1):
        print(i,end=' ')
        s=s+i
    return s
x=sumN(int(input("Enter the number")))
print(" \n Sum of n natural number=",x)

#function to calculate are of circle
def areaofcircle(r):
    return 3.14*r*r
x=areaofcircle(eval(input("Enter the radius of circle")))
print("Area of circle =",x)

#function to find factorial of a given number
def factorial(n):
    x=1
    for i in range(n,1,-1):
        print(i)
        x=x*i
    return(x)
x=factorial(eval(input("Enter the number")))
print("\n factorial =",x)


#9.To find Simple Interest
def simple(p,r,t):
    s=(p*r*t)/100
    return s
p=int(input("Enter the principle"))
r=int(input("Enter the rate"))
t=int(input("Enter the time"))
x=simple(p,r,t)
print("Simple Interest =",x)


#10 function to print average of given number
def avg(a,b,c):
    s=(a+b+c)/3
    return s
a=(int(input("Enter the number")))
b=(int(input("Enter the number")))
c=(int(input("Enter the number")))
x=avg(a,b,c)
print(x)





