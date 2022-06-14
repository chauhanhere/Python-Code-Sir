
'''
#function to check even or odd
def even(n):
    if n%2==0:
        return True
    else:
        return False
print(even(int(input("Enter the number you want to check"))))

#function to check a leap  year
def leap(n):
    if n%100==0:
        if n%400==0:
            return True
        else:
            return False
    else:
        if n%4==0:
            return True
        else:
            return False
        
print(leap(int(input("Enter the year you want to check"))))

#function to check a given string is palindrome or not
#reverse the string and check it with the original string
def palindrome(n):
    v=n[::-1]
    if n==v:
        return True
    else:
        return False
print(palindrome(input("Enter the string")))

#function to check a given number is palindrome or not
def isPalindrome(x: int):
    if x<0: #because of (-121)
        return False
    else:
        s=str(x)
        v=s[::-1]
        if(x==int(v)):
            return True
        else:
            return False
print(isPalindrome(-121))

#OR
'''
def isPalindrome(x: int):
    if x<0:
        return False
    return str(x)==str(x)[::-1]
print(isPalindrome(154.451))#Here decimal will work
'''      
#OR if we dont want to convert int into string then we can use this function

def isPalindrome(x: int):
    s=x
    if x<0:
        return False
    else:
        n=0
        while s>0:
            t=s%10
            n=n*10+t
            s=s//10
    print(x,n)
    return x==n
print(isPalindrome(15451))#Here decimal will not work

#Function to check wheather a given string is palindrone or not
def ispalindrome(s):
    for i in range(0,int(len(s)/2)):
        if s[i]==s[int(len(s))-i-1]:
            return True
    return False
print(ispalindrome(input("Enter the string")))



#function to check prime number
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return True, print("the given number is not prime")
        else:
            return print("the given number is prime")

print(isprime(int(input("Enter the number you want to check"))))

# function to check wheather a given number is in Fibonacci Series or not
import math
def perfectsquare(n):
    print(n)
    s=int(math.sqrt(n))
    return s*s==n
n=eval(input("Enter the number"))
a=5*(n*n)+4
b=5*(n*n)-4

if perfectsquare(a)or perfectsquare(b):
    print(n,"is fibonacci number")
else:
    print(n,"is not fibonacci number")


# 6.next prime of a given number

def nextprime(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%i==0:
                print(n,i)
                break
        else:
            return n
s=nextprime(eval(input("Enter the number to find next prime of that number")))
print(s,"is the next prime number")

#7.function to find n terms of fibonacci series
def fibonacci(n):
    a,b=0,1
    d=0
    for i in range(n):
        c=a+b
        d+=1
        a,b=b,c
    return c
s=fibonacci(eval(input("Enter the number to find the fibonacci series")))
print(s,"is the nth term of fibonacci number")

#8. Function to count number of digits
def count(n):
    c=0
    while n>0:
        c+=1
        n=n//10
    return c
s=count(int(input("enter the number to count its digit")))
print("Number of digits=",s)

#9.Function to count words in a given string
def countwords(n):
    a=len(n.split())
    return a
s=countwords(input("Enter the string"))
print("Number of words=",s)

#10.Function to count vowels in a given string
def countvowels(s):
    v=s.lower()
    l=v.count('a')
    k=v.count('e')
    m=v.count('i')
    c=v.count('o')
    w=v.count('u')
    return l+k+m+c+w
s=countvowels(input("Enter the string"))
print("Number of vowels=",s)

#OR

#10.Function to count vowels in a given string
def countvowels(s):
    v=s.lower()
    c=0
    for i in s:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            c+=1
    return c
s=countvowels(input("Enter the string"))
print("Number of vowels=",s)

'''


















        


    
