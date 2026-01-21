# Write a function that takes two numbers and returns their greatest common divisor (GCD).

def find_max(numbers):
    if not numbers:
        return None
    
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


nums = [45, 12, 78, 34, 90, 23]
print(f"Maximum value: {find_max(nums)}")

