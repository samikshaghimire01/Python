# Write a function that takes a list of strings as input and returns 
# a new set containing all the unique characters in all the strings.

def unique_characters(strings):
    return set(''.join(strings))

strings = ['hello', 'world', 'python']
print(unique_characters(strings))