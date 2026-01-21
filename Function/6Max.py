# Write a function that takes a list of numbers and returns the maximum value without using Python’s built-in max().

def find_max(numbers):
    if not numbers:
        return None
    
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


nums = [45, 1, 78, 34, 480, 23]
print(f"Maximum value: {find_max(nums)}")

