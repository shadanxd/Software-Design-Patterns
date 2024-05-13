# Factory method

# What we usually do?

class Goat:
    #Initialiser 
    def __init__(self) -> None:
        print("Creating Goat")
        pass
    #Method 
    def speak(self):
        print("Goat Sound")

# We create a class with certain with defined characteristsics and functions it can perform
# This Goat class can be used to initialised inhrited exported and used to make any number of goats with the keyword new 
# But what if now you have a farm with other animals or goats that need to be diffrentiated with male and female values
# Question begs how do you solve it?
        
class Chicken:
    def __init__(self) -> None:
        print("Creating Chicken")
        pass
    def speak(self):
        print("Chicken Sound")
# Keep Creating multiple classes with different object characteritics keep extending that class to 
# add more methods and so on
# We can clearly see repeated use method speak, do we need to write and repeat this a farm with 20 or more animals?
        
# Factory method solves this dilemma by seperating object definition and object creation
# It also creates a template of object creation in which each subclass can has its own characteritics 

from abc import ABC, abstractmethod

# Abstract Product with template Animal
class Animal(ABC):
    #Abstract Method with certain functionality speak not necesarrily defines what which will be further used by subclass
    @abstractmethod
    def speak(self):
        pass
# What is abstract method
# this method is the declaration of the fact that it cannot be implemented in this class itself and it needs
# a subclass to implement. Its abstracted form its orignal form

# Concrete Product
class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"


## Abstract Factory forces us to create objects of subclasses with special methods and implmentations
# Its not concerned with the Abstract class or its logic
# Thereby neately separating Object Logic its creation and its implementation

# Abstract Factory
class AnimalFactory(ABC):
    def create_animal(self):
        pass

# Concrete Factory
class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()
    
# Client Code
def main():
    # Creating a Dog
    dog_factory = DogFactory()
    dog = dog_factory.create_animal()
    print(dog.speak())  # Output: Woof!

    # Creating a Cat
    cat_factory = CatFactory()
    cat = cat_factory.create_animal()
    print(cat.speak())  # Output: Meow!

if __name__ == "__main__":
    main()


# Why do u need to separate object creatoon and implmentation
# Because a client code using this is not concerned about the logic inside what animal code has it hides extended code
# Multiple other animals can be added as subclass without affecting client code behaviour, hence better scalibility 
# Object construction is separated from object implmentation

# How easy it is to modufy and change the method of subclasss
# Pretty easy is each subclass can also be modified to change its behavior without affecting other subclasses

# What are its limitation 
#The code may become more complicated since you need to introduce a lot of new subclasses to implement the patter
    
