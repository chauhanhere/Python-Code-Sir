
for i in range(2,105):
    for n in range(2,i):
        if(i%n==0):
            break
    else:
        print(i,end=' ')





#Else will execte if break is not executed a single time
