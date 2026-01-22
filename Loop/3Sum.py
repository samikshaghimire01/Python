# Write a program to calculate the sum of all numbers in a list using a for loop.

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")