# Book class that defines the properties of a book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False  # Indicates whether the book is borrowed or not

    def borrow(self):
        if self.is_borrowed:
            print(f"The book '{self.title}' is already borrowed.")
            return False
        else:
            self.is_borrowed = True
            print(f"You have borrowed the book '{self.title}'.")
            return True

    def return_book(self):
        if not self.is_borrowed:
            print(f"The book '{self.title}' was not borrowed.")
            return False
        else:
            self.is_borrowed = False
            print(f"You have returned the book '{self.title}'.")
            return True


# Member class representing a library member
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List to store borrowed books

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book.return_book():
            self.borrowed_books.remove(book)


# Library class that holds the collection of books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")


# Example Usage:
if __name__ == "__main__":
    # Create some books
    book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
    book3 = Book("1984", "George Orwell", "9780451524935")

    # Create a library and add books
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Show all books in the library
    print("Library Books:")
    library.show_books()

    # Create a member
    member1 = Member("John Doe", "M001")

    # Member borrows a book
    print("\nJohn borrows '1984':")
    member1.borrow_book(book3)

    # Show books after borrowing
    print("\nLibrary Books After Borrowing:")
    library.show_books()

    # Member tries to borrow the same book again
    print("\nJohn tries to borrow '1984' again:")
    member1.borrow_book(book3)

    # Member returns a book
    print("\nJohn returns '1984':")
    member1.return_book(book3)

    # Show books after returning
    print("\nLibrary Books After Returning:")
    library.show_books()

    # Member borrows another book
    print("\nJohn borrows 'The Catcher in the Rye':")
    member1.borrow_book(book1)

    # Final library status
    print("\nFinal Library Books Status:")
    library.show_books()

