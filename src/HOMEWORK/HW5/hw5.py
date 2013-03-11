'''
File:        hw5.py
Author:      Eliot Carney-Seim
Date:        Mar 10, 2013 11:38:59 PM
Section:     10
Email:       eliot2@umbc.edu
Description: This program will take present the user with a menu of 4 things:
to quit, or to convert a given decimal to either binary or hexadecimal, or to 
convert an 8 bit binary code to decimal.

Assumptions: 

'''

DEBUG = True

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
                print "Please enter a Valid string."
                return False
        elif type(comparator) is str:
            return comparator
        else:
            print "Please enter a Valid string."
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
                print "Please enter a Valid integer."
                return False
        if type(comparator) is int:
            return comparator
        else:
            print "Please enter a Valid integer."
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
            print "Please enter a Valid float."
            return False
        # and if it can't be turned into an int, then it is a float.
        # and we are looking for a float, so we WANT this to throw an exception
        try:
            comparator = int(comparator)
            print "Please enter a Valid float."
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
                print "Please enter a Valid float."
                return False
        if type(comparator) is float:
            return comparator
        else:
            print "Please enter a Valid string."
            return False
    elif vtype == 'list':
        if type(comparator) is list:
            valid = True
            comparator = list(comparator)
        if comparatee is not None and valid is True:
            if comparator == comparatee:
                return True
            else:
                print "Please enter a Valid list."
                return False
        elif type(comparator) is list:
            return comparator
        else:
            print "Please enter a Valid list."
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
                print "Please enter a Valid boolean."
                return False
        elif type(comparator) is bool:
            return comparator
        else:
            print "Please enter a Valid boolean."
            return False
    elif comparator == 'Quit...':
        # returning something that isn't False, if in a while loop
        return True
    else:
        raise Exception('Invalid data type given')


def printGreeting():

    print "Hello User, please follow all instructions! The program does the\n" \
    " following: This program will take present the user with a menu of\n" \
    " 4 things: to quit, or to convert a given decimal to either binary or\n" \
    " hexadecimal, or to convert an 8 bit binary code to decimal."

def decToHex(decimal):
    print None

def decToBin(decimal):
    binary = ''
    decimal = int(decimal)
    for power in range(7, -1, -1):
        if decimal / (2 ** power) != 0:
            decimal -= 2 ** power
            binary = binary + '1'
        else:
            binary = binary + '0'
    return binary

def binToDec(binary):
    decimal = 0
    loc = 0
    # we increment down from 7 to 0, while we move up the string from 0 to 7
    for power in range(7, -1, -1):
        if binary[loc] != 0:
            decimal += (2 ** power)
        loc += 1
    return decimal

def getInput(menu, choicesList):
    gotInputBool = False
    # function to get the menu choice
    while gotInputBool == False:
       choice = raw_input(menu)
       choice = choice.upper()
       # this function will return false if not in the choicesList, else True.
       gotInputBool = cvalidate('str', choice, choicesList)
       debug(DEBUG, gotInputBool)
    return choice

def main():

    decimal = 0
    choice = ''
    input = ''
    numInputBool = False
    choicesList = ['A', 'B', 'C', 'D']
    menu = "\t[A] - Convert from Decimal to Binary\n"\
           "\t[B] - Convert from Decimal to Hexadecimal\n"\
           "\t[C] - Convert from Binary to Decimal\n"\
           "\t[D] - quit\n"\
           "What's your choice? "
    ask = "\nEnter the number: "
    results = "\nYour conversion is: "

    printGreeting()

    while choice != 'D':
        # simple function to make sure the give choice is valid.
        choice = getInput(menu, choicesList)
        if choice == 'A':
            while numInputBool == False:
                # keep asking for a decimal till the user puts one in.
                decimal = raw_input(ask)
                # will return a bool if int AND between or equal to 0 and 255.
                numInputBool = cvalidate('int', decimal, (0, 255))
            print results + str(decToBin(decimal)) + '\n'











main()
