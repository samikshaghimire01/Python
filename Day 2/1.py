# """Create a class Book with attributes title and author. 
#    Then create two different objects from this class and print their details."""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("Harry Potter", "J.K. Rowling")

print("Book 1:")
print("Title:", book1.title)
print("Author:", book1.author)

print("\nBook 2:")
print("Title:", book2.title)
print("Author:", book2.author)
