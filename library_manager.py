import os

# A list to store books (each book is a dictionary)
library = []

# Function to add a book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    
    library.append(book)
    print("Book added successfully!\n")

# Function to remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]
    print(f"Book '{title}' removed successfully!\n")

# Function to search for a book
def search_books():
    print("Search by: ")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the title: ")
        results = [book for book in library if title.lower() in book["title"].lower()]
    elif choice == "2":
        author = input("Enter the author: ")
        results = [book for book in library if author.lower() in book["author"].lower()]
    else:
        print("Invalid choice!")
        return

    if results:
        print("\nMatching Books:")
        for i, book in enumerate(results, start=1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.\n")

# Function to display all books
def display_books():
    if library:
        print("\nYour Library:")
        for i, book in enumerate(library, start=1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("Your library is empty.\n")

# Function to display library statistics
def display_statistics():
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"\nTotal books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%\n")

# Function to save library to a file
def save_library():
    with open("library.txt", "w") as file:
        for book in library:
            file.write(f"{book['title']}|{book['author']}|{book['year']}|{book['genre']}|{'yes' if book['read'] else 'no'}\n")
    print("Library saved to file.\n")

# Function to load library from a file
def load_library():
    if os.path.exists("library.txt"):
        with open("library.txt", "r") as file:
            for line in file:
                title, author, year, genre, read_status = line.strip().split("|")
                book = {
                    "title": title,
                    "author": author,
                    "year": int(year),
                    "genre": genre,
                    "read": read_status.lower() == "yes"
                }
                library.append(book)
        print("Library loaded from file.\n")
    else:
        print("No saved library found.\n")

# Main menu function
def menu():
    while True:
        print("Menu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

# Load the library from the file (if it exists) before starting the program
load_library()

# Start the menu
menu()
