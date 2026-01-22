# Write a class DataSize with init, str, and add so you can add two DataSize objects and print them nicely.

class DataSize:
    def __init__(self, value, unit="MB"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        if not isinstance(other, DataSize):
            return NotImplemented


        if self.unit != other.unit:
            raise ValueError("Cannot add DataSize objects with different units")

        return DataSize(self.value + other.value, self.unit)


size1 = DataSize(400, "MB")
size2 = DataSize(50, "MB")

total_size = size1 + size2

print(size1)
print(size2)
print("Total:", total_size)
