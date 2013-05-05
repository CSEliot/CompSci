from Book import Book
'''
File:        proj1.py
Author:      Eliot Carney-Seim
Date:        Apr 7, 2013 11:38:59 PM
Section:     10
Email:       eliot2@umbc.edu
Description: You are going to write a program to keep track of the inventory of 
a bookstore. The program will allow the user to load the inventory of the
bookstore into the memory from a file, to view the inventory in alphabetical 
order by author, to add a book to the inventory, change the quantity of 
books in the inventory, and calculate the total value of the inventory.  
'''
DEBUG = False
'''
Name: Eliot Carney-Seim
Description: simple callable debug method
Input:
debugBool - to tell wether or not to print info
info - info to be printed
Returns: True if printing, False if not
'''
def debug(debugBool, info):

    if (debugBool):
        print "\nDEBUG INFO: ", info
        return True
    return False


def cvalidate(vtype, comparator, comparatee=None):
    '''
    # This function takes the given type, and the wanted type, both as a string
    # and an option 3rd input. This function is intended for use with raw_input 
    # is used for any type. If the type matches, it will return the string
    # converted to the type, otherwise False. (can be used simply for convert).
    # for strings, the 3rd input MAY be a string/list to compare to
    # for number types, the 3rd comparatee MAY be a list of range
    # if the 3rd option is used, it will always return a boolean.
    '''

    valid = False
    if vtype == 'str':
        if comparatee is not None:
            if comparator in comparatee:
                return True
            else:
                return False
        elif type(comparator) is str:
            return comparator
        else:
            return False
    elif vtype == 'int':
        # make sure the user gave us an int, if true, change comp. to an int
        if str(comparator).isdigit():
            try:
                comparator = int(comparator)
                valid = True
            except:
                None
        if comparatee is not None and valid is True:
            rList = comparatee
            if  rList[0] <= comparator <= rList[1]:
                return True
            else:
                return False
        if type(comparator) is int:
            return comparator
        else:
            return False
    elif vtype == 'long':
        # make sure the user gave us an int, if true, change comp. to an int
        if comparator.isdigit():
            valid = True
            comparator = long(comparator)
        if comparatee is not None and valid is True:
            # comparatee is put into rList for readability purposes.
            rList = comparatee
            if  rList[0] <= comparator <= rList[1]:
                return True
            else:
                return False, comparator
        if type(comparator) is long:
            return comparator
        else:
            return False
    elif vtype == 'float':
        # if it can't be turned into a float, it isn't a word. . .
        try:
            temp = float(comparator)  # @UnusedVariable
        except ValueError:
            return False
        # and if it can't be turned into an int, then it is a float.
        # and we are looking for a float, so we WANT this to throw an exception
        try:
            comparator = int(comparator)
            return False
        except ValueError:
            valid = True
            comparator = float(comparator)
        if comparatee is not None and valid is True:
            # comparatee is put into rList for readability purposes.
            rList = comparatee
            if  rList[0] <= comparator <= rList[1]:
                return True
            else:
                return False
        if type(comparator) is float:
            return comparator
        else:
            return False
    elif vtype == 'list':
        if type(comparator) is list:
            valid = True
            comparator = list(comparator)
        if comparatee is not None and valid is True:
            if comparator == comparatee:
                return True
            else:
                return False
        elif type(comparator) is list:
            return comparator
        else:
            return False
    elif vtype == 'bool':
        # this only takes a True or False
        if type(comparator) is bool:
            valid = True
            comparator = bool(comparator)
        if comparatee is not None and valid is True:
            if comparator == comparatee:
                return True
            else:
                return False
        elif type(comparator) is bool:
            return comparator
        else:
            return False
    elif comparator == 'Quit...':
        # returning something that isn't False, if in a while loop
        return True
    else:
        raise Exception('Invalid data type given')



def printGreeting():
    print "Greeting: This program simulates the management of a library and"
    print "it's books. Please follow all instructions, thank you."
    
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:                                                                                                                                                          
# This function should ask the user for the file that 
# has the input, read the content of the file (see 
# section below about the structure of the input 
# file), and make entries into the Inventory dictionary.                                                                                           
# Inputs: 
# Inventory - The dictionary of books to add to
# filename -  the user given name of the database to get books from                                                                                                                                                                
# Returns: n/a                                                                                                                                                              
'''  
def readDatabase(Inventory):
    filename = raw_input("What's the name of the database file?")
    fileIn = open(filename, 'r')
    # for each line in file
    for line in fileIn:
        # initialize our assets, author&title are formatted in class
        tempList = line.split('$')
        author = ""
        # format the author's name
        author += tempList[0] + ", " + tempList[1]
        # format the book's title
        title = tempList[2]
        quantity = tempList[3]
        price = tempList[4]
        tempBook = Book(author, title, quantity, price)
        # we check to see if the author exists in the dictionary
        if Inventory.has_key(tempBook.get_author()):
            Inventory[tempBook.get_author()].append(Book(author, title, \
                                                         quantity, price))
        else:
            Inventory[tempBook.get_author()] = [Book(author, title, \
                                                     quantity, price)]
    None
    
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
# This function should print the menu (see the
# sample run for the content of the menu) and 
# return the user's choice.
# Inputs: option - number choice given for menu
# Returns: option                                                                                                                                                              
'''     
def printMenu():
    print """-------------------------------- 
    Enter 1 to display the inventory 
    Enter 2 to add a book 
    Enter 3 to change the qty on hand 
    Enter 4 to view the total amount 
    Enter 5 to exit 
             """
    option = raw_input("Enter your choice: ")
    return option

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
# This function should display the inventory. The 
# authors should display in alphabetical order and 
# the books by each author should also be in 
# alphabetical order.
# Inputs: Inventory - dictionary of books by author
# Outputs: list of all books in inventory alphabetically
# Returns: n/a                                                                                                                                                              
'''    
def displayInventory(Inventory):
    # get a list of the names in order
    # then for len(list(key(author))), sort the list that that author returns
    # then just do a getX for all the items. 
    authorList = sorted(Inventory)
    # get the list from the key - a loop
    for i in range(len(authorList)):
        # we now have our list of books!
        bookList = Inventory[authorList[i]]
        # sort bookList by title
        bookList = sorted(bookList, key=lambda book: book.title, reverse=False)
        # a test to make sure the list is sorted.
        for book in bookList:
            debug(DEBUG, book.get_title())
        print "\nThe Author is: {0}".format(authorList[i])
        for j in range(len(bookList)):
            #set the current book to get info from
            tmpBook = bookList[j]
            tmpTitle = tmpBook.get_title()
            tmpQty = tmpBook.get_quantity()
            tmpPrice = tmpBook.get_price()
            print "\t", 
            print "Title: ", tmpTitle, ", Qty: ", tmpQty, ", Price: ", tmpPrice 

             
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:                                                                                                                                                          
# This function should ask the user for the author's 
# name, the title of the book, the qty, and the price. 
# The new book should be added to the Inventory. 
# Make sure the qty is an int and the price is a float.
# If the book was already in the Inventory, it should 
# not be re-added.                                                                                            
# Inputs: 
# Inventory - The dictionary of books to add to
# Returns: n/a                                                                                                                                                              
''' 
def addBook(Inventory):
    lastName = ''
    firstName = ''
    bookTitle = ''
    bookPrice = 0
    bookQuantity = 0
    validInput = False
    lastName = raw_input("Please enter author's last name: ").lower()
    firstName = raw_input("Please enter the author's first name: ").lower()
    fullname = "{0}, {1}".format(lastName.title(), firstName.title())
    bookTitle = raw_input("Please enter the book's title: ").lower()
    # test to see if the title and author have a match
    if Inventory.has_key(fullname):
        for book in Inventory[fullname]:
            # test to see if any of the books have the same title
            if book.get_title().lower() == bookTitle:
                # if so, return without adding
                print "Sorry, this book is already in the Inventory."
                return
                # if none of the titles match, we can add it!
    # if they don't match, we now ask for a price and quantity
    while not(validInput):
        bookQuantity = raw_input("Please enter a quantity: ")
        # send bookQuantity to cvalidate to test for proper parameters.
        validInput = cvalidate("int", bookQuantity)
        if validInput:
            # cvalidate will return false if bookQuantity is not an int
            # and will return bookQuantity as an int if it IS.
            bookQuantity = validInput
        else:
            print "Please enter a whole number for quantity."
    validInput = False # reset the boolean
    while not(validInput):
        bookPrice = raw_input("Please enter a price: ")
        # send bookPrice to cvalidate to test for proper parameters.
        validInputInt = cvalidate('int', bookPrice)
        validInputFloat = cvalidate("float", bookPrice)
        debug(DEBUG, ('validInputInt: ', validInputInt))
        debug(DEBUG, ('validInputInt: ', validInputFloat))
        if validInputInt or validInputFloat:
            # price can be either an int or float, so we must check for both.
            # cvalidate will return false if bookPrice is not a price
            # and will return bookPrice as a float if it IS.
            validInput = True
            debug(DEBUG, validInput)
            # one of those has to be True, so we see check to see which
            # it'll also be a number, which is True to an IF statement.
            if validInputInt:
                bookPrice = validInputInt
            else:
                bookPrice = validInputFloat
        else:
            print "Please enter a number for price"
    if Inventory.has_key(fullname):
        Inventory[fullname].append(Book(fullname, bookTitle, bookQuantity, 
                                        bookPrice))
    else:
        Inventory[fullname] = [Book(fullname, bookTitle, bookQuantity,
                                    bookPrice)]

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
# This function should ask the user for the name of 
# the author and the title of the book that needs to 
# have its qty updated. Only if a valid qty is entered 
# and the book is already actually part of the 
# inventory, will the qty be updated. Error messages 
# will display otherwise.
# Inputs: 
# author,  title, quantity - user inputs
# Returns: n/a
# Outputs:
# error - if an invalid quantity is given.                                                                                                                                       
'''
def changeQty(Inventory):
    lastName = ''
    firstName = ''
    bookTitle = ''
    foundMatch = False
    validInput = False
    bookQuantity = 0
    
    lastName = raw_input("Please enter the author's last name: ").lower()
    firstName = raw_input("Please enter the author's first name: ").lower()
    fullname = "{0}, {1}".format(lastName.title(), firstName.title())
    
    if Inventory.has_key(fullname):
        bookTitle = raw_input("Please enter the book's title: ").lower()
        for book in Inventory[fullname]:
            # test to see if any of the books have the same title
            if book.get_title().lower() == bookTitle:
                foundMatch = True
                # if match is found!
                # get proper book amount from the user.
                while not(validInput):
                    bookQuantity = raw_input("Please enter a quantity: ")
                    # send bookQuantity to cvalidate to test for proper param
                    validInput = cvalidate("int", bookQuantity)
                    # 0 isn't an INT, so a special case has to be done for 0.
                    if validInput or validInput == 0:
                        # cvalidate will return false if bookQuant is not an int
                        # and will return bookQuantity as an int if it IS.
                        bookQuantity = validInput
                        # more special case for qty being 0
                        validInput = True
                    else:
                        print "Please enter a whole number for quantity."
                # with the proper book quantity, modify it!
                book.set_quantity(bookQuantity)
        # after searching through the list, if no book was found, send error
        if not(foundMatch):
            print "Sorry, no matching title was found, returning to menu."
            return
    else:
        print "Sorry, no matching name was found, returning to menu."
        return
    pass

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
# This function will calculate and print the total value of the inventory.
# Inputs: 
# Inventory
# Returns: n/a
# Outputs:
# the total amount of worth of all books currently in inventory.
'''
def calculateTotal(Inventory):
    totalPrice = 0
    
    # get a list of all the authors
    # for each author, iterate through the list given from the key
    # and add book.get_price to a total
    authorList = sorted(Inventory)
    for i in range(len(authorList)):
        for book in Inventory[authorList[i]]:
            totalPrice += (book.get_price()*book.get_quantity())
    print "The total price of the inventory is: ${0}".format(totalPrice)

def main():
    
    printGreeting()
    Inventory = {}
    readDatabase(Inventory)
    
    gettingMenu = True
    testing = True
    option = 0
    valid = True
    running = True # major driver loop boolean for the program
    
    while running:
        # --- getting menu option ---- start
        while gettingMenu:
            option = printMenu()
            # if option is not an int between 1 and 5, it'll return False.
            valid = cvalidate("int", option, [1, 5])
            # then use it to make sure it's an int, and return it converted to
            # such.
            option = cvalidate("int", option)
            if valid:
                # if valid is true, no longer getting the menu.
                gettingMenu = False
        gettingMenu = True
        # --- getting menu option ---- done
        
        if option == 1:
            displayInventory(Inventory)
        elif option == 2:
            addBook(Inventory)
        elif option == 3:
            changeQty(Inventory)
        elif option == 4:
            calculateTotal(Inventory)
        else:
            # exiting the game
            running =  False
            debug(DEBUG, option)
    
            
        
        
    bookLists = []
    while testing:
        try:
            # get a key,value pair from the dictionary, key being a list
            tempTest = Inventory.popitem()
            # print the pair
            debug(DEBUG, tempTest)
            # use the get_all method for each book within the list
            for i in range(len(tempTest[1])):
                debug(DEBUG, tempTest[1][i].get_all())
        except:
            # if Inventory.popitem() finds an empty dictionary, it throws error
            testing = False
        None

        # Grabbing the List
        # Search thru the list
        # Use a getter to find match
        # USe a setter to reset value
        # fill book w/ data
        # put in the list
        
        # check for valid prices and quantities when adding books!!
main()
