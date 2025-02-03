'''3. You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.'''
class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
            print(f'The detail as follows: \nBookname:{obj.title}\nAuthor:{obj.author}\nBirthplace:{obj.isbn}')
title=input('enter the title of the book:')
author=input('enter the name of the author:')
isbn=input('enter the birth place of the author:')
       
obj=Book(title,author,isbn)
obj.display()