'''
n=int(input("Enter the nmbers"))
a=1
s=0
while(a<=n):
    s=s+a
    a=a+1
print(s)
'''
n=289473
while n!=0:
    n,r=divmod(n,10)
    print("r=",r,"n=",n)
