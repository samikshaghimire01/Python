# Write a function that takes a list of integers as input and 
# returns a new list where each element is the product of all the other
#  elements in the list (except for itself). 

def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    
    return result

numbers = [1, 2, 3, 4]
print(product_except_self(numbers))