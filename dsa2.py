class Parrot:
    #class attribute
    species = "bird"

    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instantiate the Parrot Class  
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

#access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

#access the instances attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))


class Human:
    def __init__(self, legs, arms):
        self.legs = legs
        self.arms = arms
bob = Human(2, 2)
print(bob.legs)
print(bob.arms)

class Plane: 
    def __init__(self):
        self.wings = 2

        self.drive()
        self.flaps()
        self.wheels()

    def drive(self):
        print('Accelarating')
    
    def flaps(self):
        print('Changing flaps')

    def wheels(self):
        print('Closing wheels')

ba = Plane()

class Bug:
    def __init__(self):
        self.wings = 4

class Human:
    def __init__(self):
        self.legs = 2
        self.arms = 2
    
bob = Human()
tom = Bug()

print(tom.wings)
print(bob.arms)

f = 101
print(f)
def local():
    global f
    print(f)
    f = "changing global variable"

local()
print(f)

class Student:
    names = "Student"
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def avg(self):
        return (self.a + self.b)/2
    
    @classmethod
    def info(cls):
        return cls.names
    
    @staticmethod
    def info_1():
        return "This is a student class"
    
sl = Student(10, 20)
print(sl.avg())
print(Student.info())
print(Student.info_1())

def new_line():
    for i in range(4):
        print("\n")

# Single Inheritance
class ParentClass:
    def feature_1(self):
        print('feature_1 from ParentClass is running...')

    def feature_2(self):
        print('feature_2 from ParentClass is runnning....')
    
class ChildClass(ParentClass):
    def feature_3(self):
        print('feature_3 from ChildClass is running...')

obj = ChildClass()
obj.feature_1()
obj.feature_2()
obj.feature_3()

new_line()

# Mulitiple Inheritance
class ParentClass_1:
    def feature_1(self):
        print('feature_1 from ParentClass_1 is running...')

class ParentClass_2:
    def feature_2(self):
        print('feature_2 from ParentClass_2 is running...')

class ChildClass_2(ParentClass_1, ParentClass_2):
     def feature_3(self):
         print('feature_3 from ChildClass is running...')
    
obj_2 = ChildClass_2()
obj_2.feature_1()
obj_2.feature_2()
obj_2.feature_3()

new_line()

# Multi Level Inheritance
class ParentClass_2:
    def feature_1(self):
        print('feature_1 from ParentClass_2 is running...')

class ChildClass_2(ParentClass_2):
    def feature_2(self):
        print('feature_2 from ChildClass_2 is running...')

class ChildClass_3(ChildClass_2):
    def feature_3(self):
        print('feature_3 from ChildClass_3 is running...')

obj_3 = ChildClass_3()
obj_3.feature_1()
obj_3.feature_2()
obj_3.feature_3()

new_line()

# Heirarchical Inheritance
class ParentClass_3:
    def feature_1(self):
        print('feature_1 from ParentClass_3 is running....')

class ParentClass_4: 
    def feature_2(self):
        print('feature_2 from ParentClass_4 is running...')

class ChildClass_4(ParentClass_3, ParentClass_4):
    def feature_3(self):
        print('feature_3 from ChildClass_4 is running...')

obj_4 = ChildClass_4()
obj_4.feature_1()
obj_4.feature_2()
obj_4.feature_3()

# Polymorphism
class Square:
    side = 5

    def calculate_area(self):
        return self.side * self.side
    
class Triangle:
    base = 5
    height = 4

    def calculate_area(self):
        return 0.5 * self.base * self.height
    
sq = Square()
tri = Triangle()

new_line()
print("Area of square:", sq.calculate_area())
print("Area of triangle:", tri.calculate_area())