# Create a class Dog with a class variable species = "Canine".
#  Each object should also have its own name. Demonstrate the difference by printing both.

class Dog:
    species = "Canine"   

    def __init__(self, name):
        self.name = name  

dog1 = Dog("Bruno")
dog2 = Dog("Sheti")

print("Dog 1:")
print("Name:", dog1.name)
print("Species:", dog1.species)

print("\nDog 2:")
print("Name:", dog2.name)
print("Species:", dog2.species)
