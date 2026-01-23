#  Write a Python script to read a CSV file and print its contents row by row.

import csv

with open(r"D:\Python\Day 3\7\data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
