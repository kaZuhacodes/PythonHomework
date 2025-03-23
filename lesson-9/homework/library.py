class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    MAX_BORROWED_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_BORROWED_BOOKS:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than {Member.MAX_BORROWED_BOOKS} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed {book.title}.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

    def __str__(self):
        return f"{self.name} (Borrowed Books: {', '.join([book.title for book in self.borrowed_books]) if self.borrowed_books else 'None'})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Added book: {book.title} by {book.author}")

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        print(f"Added member: {member.name}")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException(f"Book '{title}' not found in library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        try:
            book = self.find_book(book_title)
            member.borrow_book(book)
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(e)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        try:
            book = self.find_book(book_title)
            member.return_book(book)
        except BookNotFoundException as e:
            print(e)

    def display_books(self):
        for book in self.books:
            print(book)

    def display_members(self):
        for member in self.members:
            print(member)


library = Library()


library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")


library.add_member("Alice")
library.add_member("Bob")


library.borrow_book("Alice", "1984")
library.borrow_book("Alice", "The Great Gatsby")
library.borrow_book("Alice", "To Kill a Mockingbird")


library.borrow_book("Alice", "Another Book")


library.borrow_book("Bob", "1984")


library.return_book("Alice", "1984")


library.return_book("Bob", "The Great Gatsby")


print("\nLibrary Books:")
library.display_books()
print("\nLibrary Members:")
library.display_members()
