# 20. Create a list of books. Implement add book, search book, remove book, display all books and count total books.

books = ["Python", "Java", "C++"]
books.append("HTML")
print("Search:", "Python" in books)
books.remove("Java")
print("Books:", books)
print("Total books:", len(books))