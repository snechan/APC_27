books = {"Python": "Available", "Java": "Available"}

def add_book(name):
    books[name] = "Available"

def issue_book(name):
    if name in books and books[name] == "Available":
        books[name] = "Issued"

def return_book(name):
    if name in books:
        books[name] = "Available"

def search_book(name):
    print(books.get(name, "Not found"))

def display():
    print(books)

add_book("C")
issue_book("Python")
return_book("Python")
search_book("Java")
display()