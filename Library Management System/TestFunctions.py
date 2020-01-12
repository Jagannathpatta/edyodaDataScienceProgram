# -*- coding: utf-8 -*-

"""
This file is the try and error file .
contents of this file is used at the time of testing.
Don't run this file, Run the file Final_Test_Functionalities line by line. 
"""

from Book import Book
from Catalog import Catalog
from User import Member, Librarian
from datetime import date


today = date.today()
d = today.strftime("%d/%m/%Y")
type(today)
today
newdate = date(2020, 1, 30)
newdate

type((newdate - date.today()).days)

b1 = Book('Shoe Dog','Phil Knight', '2015',312)
b1.addBookItem('123hg','H1B2')
b1.addBookItem('124hg','H1B3')

b1.printBook()

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '124hg','H1B4')
catalog.addBookItem(b, '125hg','H1B5')

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(b, '463hg','K1B2')

b = catalog.addBook('Someone','JP', '2005',298)
catalog.addBookItem(b, '842hg','J1B2')

b = catalog.addBook('13 Secrets','Robin D', '2007',188)
catalog.addBookItem(b, '363hg','I1B3')

b = catalog.addBook('World Beyond Imagination','Jeferson Lem', '2001',428)
catalog.addBookItem(b, '542hg','L1B6')

catalog.displayAllBooks()
catalog.books

m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')

librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
print (m1)
print (librarian)

m1.BooksInHand[0][1]
m1.issueBook('Shoe Dog',catalog)
m1.issueBook('Moonwalking with Einstien',catalog)
m1.issueBook('Someone',catalog)
m1.issueBook('13 Secrets',catalog)
m1.issueBook('World Beyond Imagination',catalog)
m1.issueBook('Shoe Dog',catalog)
#m1.issueBook

m1.returnBook('Shoe Dog',catalog)
m1.returnBook('Moonwalking with Einstien',catalog)
m1.returnBook('Someone',catalog)
m1.returnBook('13 Secrets',catalog)
m1.returnBook('World Beyond Imagination',catalog)


librarian.addBook(catalog ,'Moonwalking with Einstien','J Foer', '2017',318)
librarian.addBookItem(catalog, 'Moonwalking with Einstien', '463hg','K1B2')
librarian.addBookItem(catalog, 'Moonwalking with Einstien', '462hg','K1B1')


librarian.addBook(catalog ,'Someone','JP', '2005',298)
librarian.addBookItem(catalog, 'Someone', '842hg','J1B2')

librarian.addBook(catalog ,'Shoe Dog','Phil Knight', '2015',312)
librarian.addBookItem(catalog, 'Shoe Dog','123hg','H1B2')
librarian.addBookItem(catalog, 'Shoe Dog', '124hg','H1B4')
librarian.addBookItem(catalog, 'Shoe Dog','125hg','H1B5')

librarian.addBook(catalog ,'13 Secrets','Robin D', '2007',188)
librarian.addBookItem(catalog, '13 Secrets', '363hg','I1B3')


librarian.addBook(catalog ,'World Beyond Imagination','Jeferson Lem', '2001',428)
librarian.addBookItem(catalog, 'World Beyond Imagination', '542hg','L1B6')

librarian.removeBookItemFromCatalog(catalog, 'Someone' , '842hg')

librarian.removeBook(catalog ,'Shoe Dog')
catalog.searchByName('Someone')

catalog.searchByAuthor('JP')
