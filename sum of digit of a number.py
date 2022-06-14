n=int(input("Enter the number to find sum of digits"))
s=0
count=0
while n!=0:
    s=n%10
    n=n//10
    count=count+s
print(count)




#n=int(input("Enter the number to find the digits"))
#count=0
#while n!=0:
 #   count=count+1
  #  n=n//10
#print(count)
