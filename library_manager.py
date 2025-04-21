import json
import os

# 📚 In-memory library
library = []

# 📂 File to save/load data
filename = "library.json"

# ✅ Load library from file (if exists)
if os.path.exists(filename):
    with open(filename, "r") as f:
        try:
            library = json.load(f)
        except json.JSONDecodeError:
            library = []

# 🔐 Function to save library to file
def save_library():
    with open(filename, "w") as f:
        json.dump(library, f, indent=4)

# ➕ Add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print("✅ Book added successfully!")

# ➖ Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found.")

# 🔍 Search for a book
def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the search keyword: ").strip().lower()

    matches = []
    for book in library:
        if (choice == "1" and keyword in book["title"].lower()) or \
           (choice == "2" and keyword in book["author"].lower()):
            matches.append(book)

    if matches:
        print("\n📖 Matching Books:")
        for i, book in enumerate(matches, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("❌ No matching books found.")

# 📜 Display all books
def display_all_books():
    if not library:
        print("📚 Your library is empty.")
        return
    print("\n📚 Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# 📈 Display statistics
def display_stats():
    total = len(library)
    read_count = sum(1 for book in library if book["read"])
    percentage = (read_count / total * 100) if total else 0
    print(f"\n📊 Total books: {total}")
    print(f"✅ Books read: {read_count}")
    print(f"📖 Percentage read: {percentage:.1f}%")

# 🧭 Main menu loop
def main():
    while True:
        print("\n--- Personal Library Manager ---")
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
            search_book()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            display_stats()
        elif choice == "6":
            save_library()
            print("💾 Library saved to file. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
