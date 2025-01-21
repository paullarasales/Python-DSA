class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def description(self):
        return  f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    
class JackTheRusselTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Bulldog(Dog):
    def speak(self, sound="Worf"):
        return super().speak(sound)

buddy = Bulldog("Buddy", 9)
print(buddy.speak())
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


# Exercise 2
class Cat:
    species = "Russian"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"


class Ascat(Cat):
    def speak(self, sound="Meow"):
        return super().speak(sound)


kitty = Ascat("Kitty", 2)
print(kitty.speak())