
#1
def natural(n):
    if n>0:
        natural(n-1)
        print(n,end=" ")
s=natural(eval(input("Enter the number to find natural number")))

'''
#2

def natural(n):
    if n>0:
        print(n,end=" ")
        natural(n-1)
s=natural(eval(input("Enter the number to find natural number")))

#3

def odd(n):
    if n>0:
        odd(n-1)
        print(n*2-1,end=" ")
s=odd(eval(input("Enter the number to find natural number")))

#4

def oddreverse(n):
    if n>0:
        print(n*2-1,end=" ")
        oddreverse(n-1)
s=oddreverse(eval(input("Enter the number to find natural number")))

#5

def even(n):
    if n>0:
        even(n-1)
        print(n*2,end=" ")
s=even(eval(input("Enter the number to find natural number")))

#6

def evenreverse(n):
    if n>0:
        print(n*2,end=" ")
        evenreverse(n-1)
s=evenreverse(eval(input("Enter the number to find natural number")))


#7 recursive function to print sum of n natural numbers

def sumN(n):
    if n==0:
        return 0
    return n+sumN(n-1)
n=eval(input("Enter the number to find natural number"))
s=sumN(n)
print("Sum of ",n,"natural numbers=",s)


#8 recursive function to print sum of n even numbers
def sumN(n):
    if n==0:
        return 0
    return n*2+sumN(n-1)
n=eval(input("Enter the number to find natural number"))
s=sumN(n)
print("Sum of ",n,"even numbers=",s)

#9 recursive function to print sum of n odd numbers
def sumN(n):
    if n==0:
        return 0
    return n*2-1+sumN(n-1)
n=eval(input("Enter the number to find natural number"))
s=sumN(n)
print("Sum of ",n,"odd numbers=",s)

# Sum of square of n natural number

def sumN(n):
    if n==0:
        return 0
    return n*n+sumN(n-1)
n=eval(input("Enter the number to find natural number"))
s=sumN(n)
print("Sum of square of",n,"natural numbers=",s)

#10 Function to print factorial of a given number
def sumN(n):
    if n==0 or n==1:
        return 1
    return n*sumN(n-1)
n=eval(input("Enter the number to find natural number"))
s=sumN(n)
print("Factorial of",n,"natural numbers=",s)
'''













