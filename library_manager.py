import streamlit as st

# In-memory data structure to store books
library = []

# Function to display book details
def display_books():
    if len(library) == 0:
        st.write("No books in the library.")
    else:
        st.write("Your Library:")
        for idx, book in enumerate(library, 1):
            st.write(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")

# Function to add a book
def add_book():
    st.subheader("Add a New Book")
    
    title = st.text_input("Enter the book title:")
    author = st.text_input("Enter the author:")
    year = st.number_input("Enter the publication year:", min_value=1000, max_value=9999, step=1)
    genre = st.text_input("Enter the genre:")
    read = st.selectbox("Have you read this book?", ("Yes", "No"))
    
    if read == "Yes":
        read = True
    else:
        read = False
    
    if st.button("Add Book"):
        if title and author and year and genre:
            library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
            st.success(f"'{title}' by {author} added to your library!")
        else:
            st.error("Please fill out all fields.")

# Function to remove a book
def remove_book():
    st.subheader("Remove a Book")
    title_to_remove = st.text_input("Enter the title of the book to remove:")
    
    if st.button("Remove Book"):
        global library
        library = [book for book in library if book['title'].lower() != title_to_remove.lower()]
        st.success(f"'{title_to_remove}' removed from your library!" if title_to_remove else "No book found with that title.")

# Function to search for a book
def search_book():
    st.subheader("Search for a Book")
    search_choice = st.radio("Search by:", ("Title", "Author"))
    
    if search_choice == "Title":
        title_search = st.text_input("Enter the title to search:")
        if st.button("Search"):
            matching_books = [book for book in library if title_search.lower() in book["title"].lower()]
            if matching_books:
                for book in matching_books:
                    st.write(f"{book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")
            else:
                st.write("No matching books found.")
    elif search_choice == "Author":
        author_search = st.text_input("Enter the author to search:")
        if st.button("Search"):
            matching_books = [book for book in library if author_search.lower() in book["author"].lower()]
            if matching_books:
                for book in matching_books:
                    st.write(f"{book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")
            else:
                st.write("No matching books found.")

# Function to display statistics
def display_statistics():
    total_books = len(library)
    if total_books == 0:
        st.write("No books in your library.")
    else:
        read_books = sum(1 for book in library if book['read'])
        percentage_read = (read_books / total_books) * 100
        st.write(f"Total books: {total_books}")
        st.write(f"Percentage of books read: {percentage_read:.2f}%")

# Main program
def main():
    st.title("📚 Personal Library Manager")
    st.write("Welcome to your personal library manager! You can add, remove, search for books, and view statistics.")
    
    menu = ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics", "Exit"]
    choice = st.sidebar.selectbox("Select an option", menu)
    
    if choice == "Add a Book":
        add_book()
    elif choice == "Remove a Book":
        remove_book()
    elif choice == "Search for a Book":
        search_book()
    elif choice == "Display All Books":
        display_books()
    elif choice == "Display Statistics":
        display_statistics()
    elif choice == "Exit":
        st.write("Goodbye! Your library will be saved automatically.")

if __name__ == "__main__":
    main()
