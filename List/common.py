# Write a function that takes two lists 
# as input and returns a new list containing the elements that are common to both lists.

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
print(common_elements(a, b))