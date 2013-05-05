'''
File:        proj2.py
Author:      Eliot Carney-Seim
Date:        May 4th, 2013 11:38:59 PM
Section:     10
Email:       eliot2@umbc.edu
Description: This program will ask the user to enter a fully parenthesized 
expression that has non-negative integer operands and using only + - * / and ().
Your program will validate the input, use a stack to solve the fully 
parenthesized infix expression, convert the infix expression into postfix, and 
solve the postfix expression using a stack.
'''

from Stack import *

DEBUG = True

def printgreeting():
    print "Hello, this program was written by Eliot Carney-Seim, please follow"
    print "All instructions, "
    print "Enter a fully parenthesized expression that has"
    print "non-negative integer operands and using only + - * / and ()"

def debug(debugBool, info):

    if (debugBool):
        print "\nDEBUG INFO: ", info
        return True
    return False

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:                                                                                                                                                          
# This function will return False if the given type is not the asked for type,                                                                                          
# if it IS the given type, it will return the type converted into it's type.                                                                                            
# If a third variable is given, is compares the 2 variables and returns T/F.                                                                                            
# Inputs:                                                                                                                                                               
# vtype - String: tells what type you want to test for (str, int, float, etc.)                                                                                          
# comparator - String: the variable who's type you want to verify                                                                                                       
# comparatee - String: an optional input for comparing to comparator for ==.                                                                                            
# Returns:                                                                                                                                                              
# If not comparatee: False, or Comparator converted to vtype                                                                                                            
# If comparatee:  True or False                                                                                                                                         
'''
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


'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
#     Ask the user for the 
# input and validate the input to make sure it is a fully parenthesized 
# expression that has non-negative integer operands and using only + - * / 
# and (). getInput should return the validated input back to main. 
# Inputs: n/a
# Returns: validExpression -  the validated input from user                                                                                                                                                             
'''  
def getInput():
    validInput = False
    expression = '' # user given parenthesized expression, checked for validity.
    
    
    
    while not validInput:
        expression = raw_input('Please enter the expression: ')
        expressionList = expression
        
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:

# Inputs: expression - the string to test
# Returns: boolean, based on if there are any invalid characters in the list.                                                                                                                                                              
'''
def inputTest(expression):
    
    validSymbols = ['(', ')', '/', '+', '-', '*'] # for testing, excluding #s
    parenthesis = 0 # used to keep track of left and right end parenthesis.
    prevChar = '' # used to make sure we don't get a - or _ before a #
    
    for letter in expression:
            if not letter in validSymbols:
                    if not letter.isdigit():
                            return False
                    else: 
                        # it's a number, which is fine.
                        # So test to see if the character before was a 
                        pass
            else:
                # if it's valid, we should still test for 
                # - or + in front of numbers.
                # and parenthesis balance must match, so we 
                # account for that too.
                if letter is "(" or ")":
                    if letter is '(':
                        parenthesis += 1
                    if letter is ')':
                        parenthesis -= 1
                        # if the parenthesis count goes below 0
                        # that means the () was input wrong.
                        if parenthesis < 0:
                            return False
                prevChar = letter
                        
    
    
    
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
#     It should be called from main. It should take in the fully parenthesized 
# expression and evaluate it using a stack
# Inputs: 
# Returns: n/a                                                                                                                                                              
'''
def evaluateInfix(expression):
    None


'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
#     It should be called from main. It should take in the fully parenthesized 
# expression and return it as a postfix expression.
# Inputs: n/a
# Returns: postFix                                                                                                             
'''
def infixToPostfix():    
    None
    
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
#     It should be called from main. It should take in the postfix  
# expression and evaluate it using a stack
# Inputs: 
# Returns: n/a                                                                                                                                                              
'''
def evaluatePostfix():
    None

def main():
    printgreeting()
    
    myStack = Stack()
    
    debug(DEBUG, myStack    )

    stre = ''
    stre.isdig

if __name__ == '__main__':
    main()