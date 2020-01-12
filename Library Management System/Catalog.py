# -*- coding: utf-8 -*-
from Book import Book
#First Book is file & second is Class

# Class catalog object contains Books and BooItems details. 
class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []                             # stores all Book Objects
        
    #Only available to admin
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)    # Obj of class Book is created
        self.different_book_count += 1              # count of biff. book incremented
        self.books.append(b)                        # Obj is added to the books[] (List) 
        return b                                    # Obj is returned
    
    #Only available to admin
    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)                # adding the BookItem by calling the addBookItem() Method of obj Book
        
    # used to Search a Book using the name
    def searchByName(self,name):
        for book in self.books:                     # loops runs no. of Book available
            if name.strip() == book.name:           # Compairs the given name with Book obj name
                return book                         # returns the Book Obj
              
        else:                                       # if given name does not matches with any Book Obj name 
            return None                             # than return None
    
    # used to Search a Book using the author
    def searchByAuthor(self,author):
        for book in self.books:                     # loops runs no. of Book available
            if author.strip() == book.author:       # Compairs the given name with Book obj author
                return book                         # returns the Book Obj
                #book.printBook()
        else:                                       # if given name does not matches with any Book Obj name
            return None                             # than return None
    
    # used to display All book in Catalog
    def displayAllBooks(self):
        print ('Different Book Count',self.different_book_count)
        c = 0
        for book in self.books:                     # loops runs no. of Book available
            c += book.total_count                    
            book.printBook()                        # prints isbn of each BookItem by calling the printBook() Method of obj Book
        
        print ('Total Book Count',c)
        
    # used to remove a Bookitem of a Book from Catalog 
    def removeBookItem(self, name , isbn):
        book = self.searchByName(name)              # Search a Book using the name and returns a Book Obj
        book_item = book.searchBookItem(isbn)       # Search a BookItem using the isbn and returns a BookItem Obj
        book.removeBookItems(book_item)              # remove a BookItem by calling the removeBookItems(bookItem) method of Book Obj 
