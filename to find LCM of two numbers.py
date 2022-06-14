a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
for e in range(1,(a*b)+1):
    if(e%a==0 and e%b==0):
        print("Lcm==",e)
        break

