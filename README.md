# 📚 Library Management System (OOP-based in Python)

This project implements a **basic library management system** using Python and Object-Oriented Programming (OOP) concepts. It handles borrowing, returning, and listing of books (both printed and eBooks) along with user interaction and book tracking.

---

## 🧠 Features

- Add and remove books in a library
- Support for both Printed and eBooks with inheritance
- Book borrowing and return functionality
- Tracks borrowed status of each book
- User-specific borrowing list
- Book availability status shown in listings

---

## 🏗️ Classes Overview

### `Book`
Base class for all books. Contains:
- `title`, `book_id`, `author`, and `borrowed` status
- `borrow()` method to check availability
- `return_book()` to mark it as returned

### `Printed_books` (inherits `Book`)
Represents a physical book.
- Additional attribute: `pages`

### `Ebook` (inherits `Book`)
Represents a digital book.
- Additional attribute: `file_size` (in MB)

### `User`
Represents a library user.
- Attributes: `name`, `user_id`, and `books` list
- `book_borrowed(book)` method to borrow a book
- `return_book(book)` to return a borrowed book

### `Library`
Maintains a collection of books.
- `add_book(book)`: Adds a new book to the library
- `remove_book(book)`: Removes a book
- `list_books()`: Displays current books with their borrow status

---

## 🧪 Sample Usage

```python
book1 = Printed_books("Harry Potter", 1234, "J.K. Rowling", 700)
book2 = Ebook("Lord of Rings", 1456, "John Ronald", 45)

library = Library()
library.add_book(book1)
library.add_book(book2)

user1 = User("Arjun", 156)
user2 = User("Ravi", 167)

library.list_books()

user1.book_borrowed(book1)
user2.book_borrowed(book2)

library.list_books()
