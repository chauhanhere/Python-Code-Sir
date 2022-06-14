
#capitalise the first letter without disturbing any lette,appLe=AppLe
x=input("Enter the word")
s=x[0].upper()+x[1:]
print(s)
print(type(x))

#Capitalise the first letter but makes all the letter small after 1st letter,aPPle=Apple 
x=input("Enter the word")
s=x.capitalize()
print(s)

#Capitalises 1st letter of every word but not alphanumeric
def solve(s):
    x=s.split()
    return s.replace(x,x.capitalize())
print(solve("suraj chauhan 45f"))#Suraj Chauhan 45f

#Capitalises 1st letter of every word but also alphanumeric
s="suraj singh 452f"
print(s.title())#Suraj Singh 452F
