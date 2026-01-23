#Use a with statement to open a file and print all its contents.


with open(r"D:\Python\Day 3\3\gbd.txt", "r") as file:
    content = file.read()
    print(content)
