a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
if(b>a):
    for e in range(a,1,-1):
        if(b%e==0 and a%e==0):
            print("HCF=",e)
if(a>b):
    for e in range(b,1,-1): 
        if(b%e==0 and a%e==0):
            print("HCF=",e)

    
