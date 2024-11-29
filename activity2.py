# Base class
class Animal:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

# Derived classes
class Cat(Animal):
    def move(self):
        return "Domestic animal"

class Dog(Animal):
    def move(self):
        return "Barks mostly at night."

class Goat(Animal):
    def move(self):
        return "Feeds on grass."

class Chicken(Animal):
    def move(self):
        return "Lays 21 eggs in a month."

# Function to demonstrate polymorphism
def demonstrate_movement(Animal):
    print(Animal.move())

# Main program
if __name__ == "__main__":
    # List of different vehicles
    animals = [Cat(), Dog(), Goat(), Chicken()]

    # Demonstrate polymorphism
    for animal in animals:
        demonstrate_movement(animal)
