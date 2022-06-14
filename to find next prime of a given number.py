i=int(input("Enter the number"))
while True:
    i+=1
    for e in range(2,i):
        if(i%e==0):
            break
    else:
        print(i,end=' ')
        break





#Else will execte if break is not executed a single time
