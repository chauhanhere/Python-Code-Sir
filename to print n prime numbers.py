
def nextprime(n):
    while True:
        n+=1
        for i in range(2,n):
            if(n%i==0):
                break
        else:
           return n
           break
print(nextprime(int(input("Enter the number to find "))))
'''

def nprime(N):
   num,count=1,1
   while count<=N:
        num=nextprime(num)
        yield num
        count+=1
N=int(input("Enter the number "))
l=[x for x in nprime(N)]
for e in l:
    print(e)





#It will print list of n prime numbers

def nextprime(n):
    while True:
        n+=1
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            return(n)

def nprime(N):
    num,count=1,1
    while count<=N:
        num=nextprime(num)
        yield num
        count+=1
N=int(input("Enter the number "))
l=[x for x in nprime(N)]
print(l)

#To print nth prime number
x=int(input())
n,c=1,0
if (x<1 or x>999):
    print("Invalid Input")
else:
    while(c<x):
        n+=1
        for i in range(2,n+1):
            if(n%i==0):
                break
        if(i==n):
            c=c+1
    print(n)

    '''

