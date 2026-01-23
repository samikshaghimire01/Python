# Write a program to create a CSV file with columns: id, name, age, and insert 3 rows of data.
import csv

with open(r"D:\Python\Day 3\8\students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["id", "name", "age"])

    writer.writerow([1, "Samiksha", 24])
    writer.writerow([2, "Dipika", 23])
    writer.writerow([3, "Supriya", 24])

print("CSV file created successfully.")
