import os
import json

library = []

# Optional: Load from file if exists
if os.path.exists("library.txt"):
    with open("library.txt", "r") as file:
        library = json.load(file)

def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file)

def add_book():
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_input == 'yes'

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print("✅ Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    found = False
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print("✅ Book removed successfully!")
            found = True
            break
    if not found:
        print("❌ Book not found.")

def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice (1/2): ").strip()
    query = input("Enter the search text: ").strip().lower()
    found_books = []

    for book in library:
        if (choice == "1" and query in book['title'].lower()) or \
           (choice == "2" and query in book['author'].lower()):
            found_books.append(book)

    if found_books:
        print("🔍 Matching Books:")
        for i, book in enumerate(found_books, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("❌ No matching books found.")

def display_books():
    if not library:
        print("📚 Your library is empty.")
    else:
        print("📚 Your Library:")
        for i, book in enumerate(library, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

def display_statistics():
    total_books = len(library)
    if total_books == 0:
        print("📊 No books to display stats for.")
        return
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100
    print(f"📊 Total books: {total_books}")
    print(f"✅ Percentage read: {percentage_read:.2f}%")

def main_menu():
    while True:
        print("\n📖 Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("💾 Library saved to file. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
