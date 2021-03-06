# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:22:59 2020

@author: Jagannath
"""
"""
Run the code line by line for batter understanding of the outputs
"""


#from Book import Book
from Catalog import Catalog
from User import Member, Librarian
#from datetime import date

catalog = Catalog()

m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')

librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 

librarian.addBook(catalog ,'Moonwalking with Einstien','J Foer', '2017',318)
# Out[4]: 'Book Sucessfully added.'

librarian.addBookItem(catalog, 'Moonwalking with Einstien', '463hg','K1B2')
# Out[5]: 'BookItem sucessfully Added.'

librarian.addBookItem(catalog, 'Moonwalking with Einstien', '462hg','K1B1')

# Out[6]: 'BookItem sucessfully Added.'

catalog.displayAllBooks()
"""Out[7]: Different Book Count 1
Moonwalking with Einstien J Foer
463hg
462hg
Total Book Count 2 """

catalog.books
# Out[8]: [<Book.Book at 0x273b8360908>]

librarian.addBook(catalog ,'Someone','JP', '2005',298)
# Out[9]: 'Book Sucessfully added.'

catalog.displayAllBooks()
"""Out[10]: Different Book Count 2
Moonwalking with Einstien J Foer
463hg
462hg
Someone JP
Total Book Count 2 """

catalog.books
# Out[11]: [<Book.Book at 0x273b8360908>, <Book.Book at 0x273b8360dd8>]

librarian.addBookItem(catalog, 'Someone', '842hg','J1B2')
# Out[12]: 'BookItem sucessfully Added.'

librarian.addBook(catalog ,'Shoe Dog','Phil Knight', '2015',312)
# Out[13]: 'Book Sucessfully added.'

librarian.addBookItem(catalog, 'Shoe Dog','123hg','H1B2')

# Out[14]: 'BookItem sucessfully Added.'

librarian.addBookItem(catalog, 'Shoe Dog', '124hg','H1B4')

# Out[15]: 'BookItem sucessfully Added.'

librarian.addBookItem(catalog, 'Shoe Dog','125hg','H1B5')

# Out[16]: 'BookItem sucessfully Added.'

librarian.addBook(catalog ,'13 Secrets','Robin D', '2007',188)

# Out[17]: 'Book Sucessfully added.'

librarian.addBookItem(catalog, '13 Secrets', '363hg','I1B3')

# Out[18]: 'BookItem sucessfully Added.'

librarian.addBook(catalog ,'World Beyond Imagination','Jeferson Lem', '2001',428)

# Out[19]: 'Book Sucessfully added.'

librarian.addBookItem(catalog, 'World Beyond Imagination', '542hg','L1B6')

# Out[20]: 'BookItem sucessfully Added.'

print (m1)

# Out[21]: Vish Bangalore std1233

m1.BooksInHand
# Out[22]: []

catalog.displayAllBooks()
""" Out[23]: Different Book Count 5
Moonwalking with Einstien J Foer
463hg
462hg
Someone JP
842hg
Shoe Dog Phil Knight
123hg
124hg
125hg
13 Secrets Robin D
363hg
World Beyond Imagination Jeferson Lem
542hg
Total Book Count 8 """

catalog.books

""" Out[24]: 
[<Book.Book at 0x273b8360908>,
 <Book.Book at 0x273b8360dd8>,
 <Book.Book at 0x273b833c160>,
 <Book.Book at 0x273b833c518>,
 <Book.Book at 0x273b833c588>] """

print (m1)
# Out[25]:Vish Bangalore std1233

m1.issueBook('Shoe Dog',catalog)
# Out[26]: 'Book issued Sucessfully'

m1.BooksInHand
# Out[27]: [(<BookItem.BookItem at 0x273b833c048>, datetime.date(2020, 1, 12))]

catalog.displayAllBooks()
""" Out[28]: Different Book Count 5
Moonwalking with Einstien J Foer
463hg
462hg
Someone JP
842hg
Shoe Dog Phil Knight
124hg
125hg
13 Secrets Robin D
363hg
World Beyond Imagination Jeferson Lem
542hg
Total Book Count 7 """

m1.issueBook('Moonwalking with Einstien',catalog)
m1.issueBook('Someone',catalog)

# Out[29]: 'Book issued Sucessfully'

m1.BooksInHand
""" Out[30]: 
[(<BookItem.BookItem at 0x273b833c048>, datetime.date(2020, 1, 12)),
 (<BookItem.BookItem at 0x273b8360940>, datetime.date(2020, 1, 12)),
 (<BookItem.BookItem at 0x273b8360fd0>, datetime.date(2020, 1, 12))] """

catalog.displayAllBooks()
""" Out[31]: Different Book Count 5
Moonwalking with Einstien J Foer
462hg
Someone JP
Shoe Dog Phil Knight
124hg
125hg
13 Secrets Robin D
363hg
World Beyond Imagination Jeferson Lem
542hg
Total Book Count 5 """

m1.issueBook('13 Secrets',catalog)
# Out[32]: 'Book issued Sucessfully'

m1.issueBook('World Beyond Imagination',catalog)

# Out[33]: 'Book issued Sucessfully'

m1.BooksInHand
""" Out[34]: 
[(<BookItem.BookItem at 0x273b833c048>, datetime.date(2020, 1, 12)),
 (<BookItem.BookItem at 0x273b8360940>, datetime.date(2020, 1, 12)),
 (<BookItem.BookItem at 0x273b8360fd0>, datetime.date(2020, 1, 12)),
 (<BookItem.BookItem at 0x273b833c550>, datetime.date(2020, 1, 12)),
 (<BookItem.BookItem at 0x273b833c748>, datetime.date(2020, 1, 12))] """

catalog.displayAllBooks()
""" Out[35]: Different Book Count 5
Moonwalking with Einstien J Foer
462hg
Someone JP
Shoe Dog Phil Knight
124hg
125hg
13 Secrets Robin D
World Beyond Imagination Jeferson Lem
Total Book Count 3 """

m1.issueBook('Shoe Dog',catalog)

# Out[36]: 'Already Issued Too many Books. To get another you should first return One.'

m1.returnBook('Moonwalking with Einstien',catalog)

# Out[37]: 'Book Sucessfully returned0'

catalog.displayAllBooks()
""" Out[38]:Different Book Count 5
Moonwalking with Einstien J Foer
462hg
463hg
Someone JP
Shoe Dog Phil Knight
124hg
125hg
13 Secrets Robin D
World Beyond Imagination Jeferson Lem
Total Book Count 4 """

m1.returnBook('Moonwalking with Einstien',catalog)

# Out[39]: 'This book is not issued by you'

m1.returnBook('Shoe Dog',catalog)

# Out[40]: 'Book Sucessfully returned0'

m1.BooksInHand
""" Out[41]: 
[(<BookItem.BookItem at 0x273b8360fd0>, datetime.date(2020, 1, 12)),
 (<BookItem.BookItem at 0x273b833c550>, datetime.date(2020, 1, 12)),
 (<BookItem.BookItem at 0x273b833c748>, datetime.date(2020, 1, 12))] """

m1.issueBook('Shoe Dog',catalog)

# Out[42]: 'Book issued Sucessfully'

catalog.searchByName('Someone')

# Out[43]: <Book.Book at 0x20c684252b0>

catalog.searchByAuthor('JP')

# Out[44]: <Book.Book at 0x20c684252b0>

catalog.displayAllBooks()

""" Out[45]: Different Book Count 5
Moonwalking with Einstien J Foer
463hg
462hg
Someone JP
842hg
Shoe Dog Phil Knight
123hg
124hg
125hg
13 Secrets Robin D
363hg
World Beyond Imagination Jeferson Lem
542hg
Total Book Count 8 """

librarian.removeBookItemFromCatalog(catalog, 'Someone' , '842hg')

# Out[46]: 'BookItem sucessfully removed'

catalog.displayAllBooks()

""" Out[47]: Different Book Count 5
Moonwalking with Einstien J Foer
463hg
462hg
Someone JP
Shoe Dog Phil Knight
123hg
124hg
125hg
13 Secrets Robin D
363hg
World Beyond Imagination Jeferson Lem
542hg
Total Book Count 7 """

librarian.removeBook(catalog ,'13 Secrets')

# Out[48]: 'Book sucessfully removed'

catalog.displayAllBooks()

""" Out[49]: Different Book Count 5
Moonwalking with Einstien J Foer
463hg
462hg
Someone JP
Shoe Dog Phil Knight
123hg
124hg
125hg
World Beyond Imagination Jeferson Lem
542hg
Total Book Count 6 """

librarian.removeBook(catalog ,'Shoe Dog')

# Out[50]: 'Book sucessfully removed'

catalog.displayAllBooks()

""" Out[51]: Different Book Count 5
Moonwalking with Einstien J Foer
463hg
462hg
Someone JP
World Beyond Imagination Jeferson Lem
542hg
Total Book Count 3 """
