'''
#1 To print binary of a given number
def binary(n):
    if n==0:
        return 0
    binary(n//2)
    print(n%2,end="")
s=binary(eval(input("Enter the number to find the abinary")))

s=246
print("\n",bin(s))

#2 To print octal of a given number
def octal(n):
    if n==0:
        return 0
    octal(n//8)
    print(n%8,end="")
s=octal(eval(input("Enter the number to find the abinary")))


s=25
print("\n",oct(s))
'''
#3 To print sum of square of n natural numbers
def sums(n):
    if n==0:
        return 0
    return n*n+sums(n-1)
s=sums(eval(input("Enter the number to find square")))
print(s)
'''
#4 To print nth terms of fibonacci series
def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
n=fibonacci(eval(input("Enter the number")))
print(n)

#To print fibonacci series upto n 
def fibonacci(n):
    if n==1:
        return 0#1st place =0
    if n==2:
        return 1#2nd place =1
    return fibonacci(n-1)+fibonacci(n-2)
n=eval(input("Enter the number"))
for i i4157n range(1,n+1):
    print(fibonacci(i),end=" ")

#5 To find HCF of two numbers
def HCF(a,b):
    if b==0:
        return a
    return (HCF(b,a%b))
s=HCF(eval(input("Enter the 1st number")),eval(input("Enter the 1st number")))
print(s)

#6 To print sum of digits
def digitsum(n):
    if n<10:
        return n
    return n%10+digitsum(n//10)
n=digitsum(eval(input("Enter the number")))
print(n)
    

'''















