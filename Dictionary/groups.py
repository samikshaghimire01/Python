# Write a function that takes a list of dictionaries as input, where each dictionary represents
# a person with keys 'name' and 'age', and returns a new dictionary where the keys are the ages 
# and the values are lists of names that correspond to that age.


def group_by_age(people):
    age_dict = {}
    for person in people:
        age_dict.setdefault(person['age'], []).append(person['name'])
    return age_dict

people = [
    {'name': 'Alice', 'age': 25}, 
    {'name': 'Bob', 'age': 30}, 
    {'name': 'Charlie', 'age': 25}
]
print(group_by_age(people))