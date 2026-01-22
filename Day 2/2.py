# """Write a Laptop class with attributes brand and price.
#    Create 3 objects and store them in a list. Print the list in a readable way (e.g., Dell - $800)"""

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

laptop1 = Laptop("Dell", 800)
laptop2 = Laptop("Lenovo", 750)
laptop3 = Laptop("Apple", 1200)

laptops = [laptop1, laptop2, laptop3]

for laptop in laptops:
    print(f"{laptop.brand} - ${laptop.price}")
