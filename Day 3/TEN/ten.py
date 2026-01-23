# Write a Python program to read a JSON file containing a list of users and print only their names.

import json

with open(r"D:\Python\Day 3\TEN\St.json", "r") as file:
    users = json.load(file)

for user in users:
    print(user["name"])
