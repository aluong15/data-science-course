# **Inheritance**: Write a Python program demonstrating inheritance.

class Animal:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animal sound!")

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Arf!")


# Dog object created and initialized
dog_1 = Dog("Temmie","Pomeranian")
print(dog_1.name)
dog_1.make_sound()

# Generic Animal object created and initialized
animal_1 = Animal("Pengu")
print(animal_1.name)
animal_1.make_sound()

    