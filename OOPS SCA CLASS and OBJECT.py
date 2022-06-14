'''
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*math.pow(self.radius,2)
class Cylinder(Circle):
    def __init__(self,radius,height):
        super().__init__(radius)
        self.height=height
    def area(self):
        return 2*super().area()*math.tau*self.radius*self.height #super() exempted us from writing math.pi*math.pow(self.radius,2) many times
    def volume(self):
        return super().area()*self.height
obj=Cylinder(10,20)   
print("Area of Cylindr",obj.area())
print("Volume of Cylinder",obj.volume())
print("Area of Circle",Circle.area(obj))


#Multilevel Inheritance

class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return f"Name:{self.name},age:{self.age}"

class Emp(Person):
    def __init__(self,age,name,id,sal):
        super().__init__(age,name)
        self.sal=sal
        self.id=id
    def income(self):
        return self.sal
    def __str__(self):
        return f"{super().__str__()},sal:{self.sal},id:{self.id}"
class manager(Emp):
    def __init__(self,age,name,id,sal,bonus):
        super().__init__(age,name,id,sal)
        self.bonus=bonus
    def income(self):
        return super().income()+self.bonus
    def __str__(self):
        return f"{super().__str__()},bonus:{self.bonus}"
obj=manager(24,"Suraj",101,101000,50000)
print(obj)
print("Salary=",Emp.income(obj))
print("Total income",obj.income())

'''

#Hierarcial Inheritance

class college:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Name:{self.name},Age:{self.age}"
class Teacher(college):
    def __init__(self,name,age,sal):
        super().__init__(name,age)
        self.sal=sal
    def __str__(self):
        return f"{super().__str__()},sal:{self.sal}"
class Student(college):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks
    def __str__(self):
        return f"{super().__str__()},marks:{self.marks}"
t=Teacher("Suraj",21,100000)
s=Student("Amit",18,200)
print(t,s)
member=[t,s]
for m in member:
    print(type(m),m)

#Multiple Inheritance in Page,MRO()
    

















        
