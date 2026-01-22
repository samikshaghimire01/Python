# Create a class MathOps with:    
# an instance method square(self, x)
# a classmethod cube(cls, x)
# a staticmethod is_even(x)

class MathOps:
    def square(self, x):
        return x * x

    @classmethod
    def cube(cls, x):
        return x * x * x

    @staticmethod
    def is_even(x):
        return x % 2 == 0

math = MathOps()

print("Square:", math.square(4))      
print("Cube:", MathOps.cube(3))       
print("Is Even:", MathOps.is_even(6)) 
