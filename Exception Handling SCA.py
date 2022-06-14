'''
while True:
    try:
        a=int(input("Enter 1st number"))
        b=eval(input("Enter 2nd number"))
        c=a/b
        print("Div is",c)
        break
    except ZeroDivisionError:
        print("Denominator must not be zero.")
    except ValueError:
        print("Please input integer only.")
print(a)
print("Sum =",a+b) #we can write that code here which is not dependent on any input.


a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
try:
    c=a/b
    print("Div is",c)
except ZeroDivisionError:
    print("Denominator must not be zero.")
d=a+b
print("Sum is",d)


#raise keyword
while True:
    try:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        if a<=0 or b<0:
            raise Exception("Negative numbers are not allowed.try Again")
        c=a/b
        print("Div is",c)
        break
    except ZeroDivisionError:
        print("Denominator must not be zero.")
    except ValueError:
        print("Please input integer only.")
    except Exception as ex:
        print(ex)

#Creting user defined exception

class NegativeNumberException(Exception):
    pass
while True:
    try:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        if a<=0 or b<0:
            raise NegativeNumberException("Negative numbers are not allowed.try Again")
        c=a/b
        print("Div is",c)
        break
    except ZeroDivisionError:
        print("Denominator must not be zero.")
    except ValueError:
        print("Please input integer only.")
    except NegativeNumberException as ex:
        print(ex)       
'''
#Else with the try keyword

while True:
    try:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        c=a/b
        print("Div is",c)
    except ZeroDivisionError:
        print("Denominator must not be zero.")
    #replaced ValueError Exception to check the finally block execution
    else:
        print("There is no exception in the code.Else only Executes when there is no exception in code")
        break #If a=5 and b=0 then else will not executed because there is exception in code
    finally:#If python DEH executes then finally printed first then error message,a=bhoapl then valueError thats why finally will get executed first
        print('Finally Executec Every time if there is exception or not')
