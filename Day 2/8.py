# Extend the Dog class with a counter (class variable) that tracks 
# how many dogs have been created so far.

class Dog:
    species = "Canine"   
    count = 0            

    def __init__(self, name):
        self.name = name     
        Dog.count += 1       

dog1 = Dog("Bruno")
dog2 = Dog("Sheti")

print("Species:", Dog.species)
print("Dog names:", dog1.name, dog2.name)
print(" Number of total dogs created:", Dog.count)
