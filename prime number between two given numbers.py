n=int(input("Enter the starting number"))
i=int(input("Enter the last number"))
for e in range(n,i+1):
    for s in range(n,e):
        if(e%s==0):
            break
    else:
        print(e,end=' ')





#Else will execte if break is not executed a single time
