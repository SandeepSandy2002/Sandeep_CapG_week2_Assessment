# Base class
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass Dog
class Dog(Animal):
    ## def __init__(self) method overridden
    def speak(self):
        return "BOw"

# Subclass Cat
class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog()
cat = Cat()
print(f"Dog says: {dog.speak()}")
print(f"Cat says: {cat.speak()}")
