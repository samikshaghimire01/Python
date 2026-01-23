# Copy contents from source file to destination file

with open(r"D:\Python\Day 3\5\source.txt", "r") as source_file:
    content = source_file.read()

with open(r"D:\Python\Day 3\5\destination.txt", "w") as destination_file:
    destination_file.write(content)

print("File copied successfully.")
