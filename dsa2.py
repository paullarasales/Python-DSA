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