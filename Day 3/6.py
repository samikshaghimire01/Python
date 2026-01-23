#  Write a program to count how many lines, words, and characters are in a given text file.

with open(r"D:\Python\Day 3\3\gbd.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)
word_count = 0
char_count = 0

for line in lines:
    word_count += len(line.split())
    char_count += len(line)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)
