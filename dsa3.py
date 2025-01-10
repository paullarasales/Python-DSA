class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def description(self):
        return  f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)

print(miles.description())
print(miles.speak("Arf Arf"))

names = ["Miles", "Buddy", "Jack"]
print(names)
print(miles)

# Exercice 1
# Create a Car Class
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def describe(self):
        return f"The {self.color} has {self.mileage} miles"

car_1 = Car("Blue", 20000)
car_2 = Car("Red", 30000)

print(car_1.describe())
print(car_2.describe())