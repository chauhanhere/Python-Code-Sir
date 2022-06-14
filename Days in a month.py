m=int(input("Enter the month in numeric format"))
if(m==1 and m==3):
    print("The days =31")
elif(m==5 and m==7):
    print("The days =31")
elif(m==8 and m==10):
    print("The days =31")
elif(m==12):
    print("The days =31")
elif(m==4 and m==6):
    print("The days =30")
elif(m==9 and m==11):
    print("The days =30")
elif(m==2):
    print("The month is a leap month,days=28,29")
else:
    print("Invalid month number")
