def nextprime(n):
    while True:
        n+=1
        for i in range(2,n):
            if (n%i==0):
                break
        else:
            return (n)

def nprime(N):
    count,num=1,1
    while count<=N:
        num=nextprime(num)
        yield num
        count+=1
N=int(input("Enter the number "))
l=[x for x in nprime(N)]
print(l)
