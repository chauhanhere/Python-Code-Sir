m=int(input("Enter the number of math"))
s=int(input("Enter the number of science"))
e=int(input("Enter the number of English"))
h=int(input("Enter the number of Hindi"))
t=int(input("Enter the number of Sanskrit"))
total=(m+s+e+h+t)/5
if(total>33):
    print("Pass")
    print("Percentage=",total)
    if(total>60):
        print("First Division")
    elif(total>45 and total<60):
        print("Second Division")
    elif(total>33 and total<45):
        print("Third Division")
else:
    print("Fail")
    print("Percentage=",total)
