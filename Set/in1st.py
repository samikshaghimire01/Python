# Write a function that takes two lists as input and returns a new set 
# containing the elements that are in the first list but not in the second list.


def difference_elements(list1, list2):
    return set(list1) - set(list2)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(difference_elements(list1, list2))