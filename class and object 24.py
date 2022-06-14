
#question number 1
class student:
    def __init__(student):
        student.roll=45
        student.name=input("Enter the name of student")
        student.sam=5
        student.branch="ECE"
c=student()
print(c.roll,c.name)
x=student()
x.name="Dinesh"
print(x.sam,x.branch,x.name)

#2
class Employee:
    leaves=8
    def printdetails(self):
        return f"The name is {self.name}rollno is{self.rollno} salary is {self.salary} role is {self.work}"
harry=Employee()
marry=Employee()
harry.name="Suraj"
harry.salary=562.14
harry.work="Teacher"
harry.rollno=34

marry.name="Raj"
marry.salary=5622.14
marry.work="Suraj"
marry.rollno=54
harry.leaves=12
print(harry.leaves,harry.__dict__,"\n",marry.__dict__)
print(Employee.__dict__)
print(harry.printdetails())
print(marry.printdetails())


class Employee:
    def __init__(self,aname,aroll):
        self.name=aname
        self.roll=aroll
        print('the name is',self.name)
        print('and roll is',self.roll)
s=Employee()
s.aname=input('Enter the name of employee')
s.salary=87
print(Employee(s.aname,s.aroll),Employee(s.aname,s.aroll))








