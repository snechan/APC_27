books = {}

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    books[book_id] = [title, author, True]
    print("Book added.")

def search_book():
    book_id = input("Enter book ID: ")
    if book_id in books:
        print(books[book_id])
    else:
        print("Book not found.")

def issue_book():
    book_id = input("Enter book ID: ")
    if book_id in books and books[book_id][2]:
        books[book_id][2] = False
        print("Book issued.")
    else:
        print("Book unavailable.")

def return_book():
    book_id = input("Enter book ID: ")
    if book_id in books:
        books[book_id][2] = True
        print("Book returned.")
    else:
        print("Book not found.")

def display_books():
    for book_id, details in books.items():
        if details[2]:
            print(book_id, details)

while True:
    print("\n1.Add 2.Search 3.Issue 4.Return 5.Display 6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_books()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")