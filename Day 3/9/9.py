#  Write a Python program to convert a dictionary into a JSON string and save it to a file.

import json

data = {
    "id": 1,
    "name": "Samiksha",
    "age": 24,
    "city": "Kathmandu"
}

with open("D:\Python\Day 3\9\data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Dictionary successfully saved as JSON.")
