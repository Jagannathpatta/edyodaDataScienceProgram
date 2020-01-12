# -*- coding: utf-8 -*-
from Catalog import Catalog
from datetime import date

# Super Class
class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

# Sub Class
class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.BooksInHand = []
        self.fine = 0

        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,name,cat,days=10):
        if len(self.BooksInHand) < 5 and self.fine < 250:
            catalog = Catalog()
            catalog = cat
            for book in catalog.books:
                if book.name == name and book.total_count > 0:
                    self.BooksInHand.append((book.book_item[0] , date.today()))
                    book.book_item.pop(0)
                    book.total_count -= 1 
                    return 'Book issued Sucessfully'
                elif book.name == name and book.total_count == 0:
                    return 'Book currently Not Available'   
        
        else:
            return 'Already Issued Too many Books or You have fine to pay. To get another you should first return One Book or pay the fine.'
    
    #assume name is unique
    def returnBook(self,name,cat):
        
        for bih in self.BooksInHand:
            
            if bih[0].book.name == name:
                catalog = Catalog()
                catalog = cat
                Days = abs((bih[1] - date.today()).days)
                if Days > 10:
                    self.fine = (Days - 10) * 5
                    return 'Fine amount is Rs.' + str(self.fine)
                    
                elif Days <= 10:
                    for bk in catalog.books:
                        if bk.name == name:
                            bk.book_item.append(bih[0])
                            bk.total_count += 1
                            self.BooksInHand.remove(bih)
                            return 'Book Sucessfully returned after ' + str(Days) +' days.'
        else:
            return 'This book is not issued by you'
                    
        

# Sub Class
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,cat,name,author,publish_date,pages):
        catalog = Catalog()
        catalog = cat
        catalog.addBook(name,author,publish_date,pages)
        return 'Book Sucessfully added.'
    
    def addBookItem(self ,cat, name, isbn,rack):
        catalog = Catalog()
        catalog = cat
        
        for book in catalog.books:
            if book.name == name:
                catalog.addBookItem(book ,isbn, rack)
                return 'BookItem sucessfully Added.'
                    
        else:
            return "No such book in the Catalog first add the book into the Catalog and than BookItem."
        
    
    def removeBook(self,cat ,name):
        catalog = Catalog()
        catalog = cat
        book = catalog.searchByName(name)
        if book != None:
            catalog.books.remove(book)
            return 'Book sucessfully removed'
        else:
            return 'No such book is availabel in catalog '
    
    def removeBookItemFromCatalog(self,cat, name , isbn):
        catalog = Catalog()
        catalog = cat
        catalog.removeBookItem(name , isbn)
        return 'BookItem sucessfully removed'
    
        