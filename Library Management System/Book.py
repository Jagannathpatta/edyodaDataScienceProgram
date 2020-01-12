# -*- coding: utf-8 -*-

from BookItem import BookItem
#First BookItem is file & second is Class
# class BookItem is the real life object that is been exchanged between users.

# class Book is something that is imaginary or things that not exist.
class Book:
    def __init__(self,name,author,publish_date,pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0                    # keeps the total count of BookItems 
        self.book_item = []                     # stores all BookItem Objects
       
    # used to add BookItem of a perticular Book
    def addBookItem(self,isbn,rack):
        b = BookItem(self,isbn,rack)            # Obj of BookItem is Created
        self.book_item.append(b)                # Obj added to book_item[] (list)
        self.total_count +=1                    # total count incremented
    
    # used to print the Book name and all the BookItems of that Book
    def printBook(self):
        print (self.name,self.author)
        for book_item in self.book_item:        # loops runs no. of BookItems available
            print (book_item.isbn)              # and prints isbn of each BookItem
    
    # used to Search a BookItem of a Book using the isbn
    def searchBookItem(self,isbn):
        for book_item in self.book_item:        # loops runs no. of BookItems available
            if isbn.strip() == book_item.isbn:  # compair the given isbn with each BookItem's isbn  
                return book_item                # and returns the BookItem Obj
                
    # used to remove a BookItem 
    def removeBookItems(self, book_item):
        if book_item in self.book_item:         # Checks wheather given BookItem Obj is in book_item[] (list)
            self.book_item.remove(book_item)    # and removes that BookItem obj 
            self.total_count -=1    
