class Book:
    def __init__(self,title,book_id,author):
        self.title = title
        self.book_id = book_id
        self.author = author
        self.borrowed = False

    def borrow(self):
        if not self.borrowed :
            self.borrowed = True
            print(f"{self.title} is borrowed")
            return True
        else :
            print("Book is available")

    def return_book(self):
            self.borrowed = False 

class Printed_books(Book):
    def __init__(self,title,book_id,author,pages):
        super().__init__(title,book_id,author)
        self.pages = pages

class Ebook(Book):
    def __init__(self,title,book_id,author,file_size):
        super().__init__(title,book_id,author)
        self.file_size = file_size       
    
class User :
    def __init__(self,name,user_id):
        self.__name = name
        self.user_id = user_id
        self.books = []
    
    def book_borrowed(self,book):
        if book.borrow():
            self.books.append(book.title)
            print(f"{book.title} is borrowed by {self.user_id}") 
        else:
            print("Book not available")

    def return_book(self,book):
        if book in self.books :
            book.return_book()
            self.books.remove(book)   
            print(f"{self.user_id} returned {book.title}")  
        else:
            print("Book was not borrowed")

class Library :
    def __init__(self):
        self.book = []

    def add_book(self,book):
        self.book.append(book)
        print(f"{book.title} is added to library")

    def remove_book(self,book):
        if book.title in self.book :
            self.book.remove(book)
            print(f"{book.title} is removed from library")
        else :
            print("Book not in library")

    def list_books(self):
        for book in self.book:
            status = "Borrowed" if book.borrowed else "Available"
            print(f"{book.title} by {book.author} - {status}")                   

book1 = Printed_books("Harry Potter" , 1234 , "J.K.Rowling" , 700)
book2 = Ebook("Lord of Rings", 1456 , "John Ronald" , 45)

library = Library()
library.add_book(book1)
library.add_book(book2)

user1 = User("Arjun" , 156)
user2 = User("Ravi", 167)
library.list_books()

user1.book_borrowed(book1)
user2.book_borrowed(book2)
library.list_books()
