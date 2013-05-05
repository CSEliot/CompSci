'''
File:        Book.py
Author:      Eliot Carney-Seim
Date:        Apr 18, 2013 11:38:59 PM
Section:     10
Email:       eliot2@umbc.edu
Description: This class is an object containing relevant identities: the title,
the quantity, and the price. 
'''

class book():
    
    def __init__(self, author, title, quantity, price):
        self.author = str(author).title()
        self.title = str(title).title()
        self.quantity = int(quantity)
        self.price = float(price)

    def get_all(self):
        return self.author, self.price, self.quantity, self.title

    def get_author(self):
        return self.author


    def get_title(self):
        return self.title


    def get_quantity(self):
        return self.quantity


    def get_price(self):
        return self.price


    def set_author(self, value):
        self.author = value


    def set_title(self, value):
        self.title = value


    def set_quantity(self, value):
        self.quantity = value


    def set_price(self, value):
        self.price = value


    def del_author(self):
        del self.author


    def del_title(self):
        del self.title


    def del_quantity(self):
        del self.quantity


    def del_price(self):
        del self.price

    author = property(get_author, set_author, del_author, "book author")
    title = property(get_title, set_title, del_title, "book title")
    quantity = property(get_quantity, set_quantity, del_quantity, "# in stock")
    price = property(get_price, set_price, del_price, "book price")
        
    