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
        expression = raw_input('\nPlease enter the expression: ')

        # used later for when testing if there is only space between 2 numbers.        
        origExpression = expression.split()
        prevChar = ''
        
        # a simple set of actions to remove ALL whitespace from expression:
        emptyStr = ''
        expList = expression.split()
        #.join will iterate through the expList, and for each character, 'append'
        # it to the list, with a seperator being Null, or emptyStr.
        expression = emptyStr.join(iter(expList))
        debug(DEBUG, expression)
        
        
        # if wordTest passes True, turn validInput to True.
        if allTests(expression) is not False:
            validInput = True

        
        # a quick pre-check to make sure no numbers are entered w/ space between
        for char in origExpression:
            if char.isdigit():
                if char.isdigit() and prevChar.isdigit():
                    validInput = False
                    print "Sorry, this program cannot work with this input."
                    debug(DEBUG, 'STOPPED IN origEXPRESSION test')
                else:
                    prevChar = char
    debug(DEBUG, "ALL VALID, KEEP TESTING")
    debug(DEBUG, ('ANSWER: ', eval(expression)))
    return expression
        
def allTests(expression):
    valid = True # a variable to increase readability.

    if wordTest(expression) is not valid:
        return False
    debug(DEBUG, "wordTest passed")
    if plusTest(expression) is not valid:
        return False
    debug(DEBUG, "plusTest passed")
    if minusTest(expression) is not valid:
        return False
    debug(DEBUG, "minusTest passed")
    if parenthTest(expression) is not valid:
        return False
    debug(DEBUG, "parenthTest passed")
    # if we get to this point, all tests passed, so return valid!
    return valid
    
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:

# Inputs: expression - the string to test
# Returns: boolean, based on if there are any invalid characters in the list.                                                                                                                                                              
'''
def wordTest(expression):
    
    invalid = False # legibility variable
    valid = True # legibility variable
    validSymbols = ['(', ')', '/', '+', '-', '*'] # for testing, excluding #s
    
    # ** is a special case, it's validsymbols but invalid operation
    # so we have to test for it individually
    if '**' in expression:
        print "Sorry, this program cannot work with this "+\
              "input."
        return invalid
    
    # go through the whole expression, WEAVE for errors.
    for char in expression:
        if not char in validSymbols:
                if not char.isdigit():
                        print "Sorry, this program cannot work with this "+\
                              "input."
                        return invalid
                else: 
                    # it's a number, which is fine.
                    pass
        else:
            #it is a char in the validSymbols list, so we say it's fine.
            pass
    # if everything passes, the expression loop is over and we return True.
    return valid

def plusTest(expression):
    
    i=0
    prePos = i-1 #test to see if previous char is a plus
    prePrePos = prePos - 1 # test to see if next previous char is a plus
    invalid = False # legibility variable
    valid = True # legibility variable
    operations = ['+', '-', '*', '/']

# if an equation is parenthesized correctly, then pos -1 will never be <0

    for i in range(len(expression)):
        if expression[i].isdigit():
            prePos = i-1
            debug(DEBUG, ('prePos: ', expression[prePos]))
            if expression[prePos] is '+':
                prePrePos = prePos - 1
                # check again to make sure it isn't negative.
                if prePrePos >= 0:
                    debug(DEBUG, ('prePos: ', expression[prePrePos]))
                    if expression[prePrePos] in operations:
                        # basically if a plus then operation come before
                        # a number, then SEND FALSE.
                        print "Please don't use + for positive numbers"
                        return invalid
                else:
                    # if prePrePos DOES go into the negatives, that means we
                    # it probably looks like "+x...", which is still in front.
                    print "Please don't use + for positive numbers"
                    return invalid                    
    return valid

def minusTest(expression):
    
    i=0
    prePos = i-1 #test to see if previous char is a plus
    prePrePos = prePos - 1 # test to see if next previous char is a plus
    invalid = False # legibility variable
    valid = True # legibility variable
    operations = ['+', '-', '*', '/']

    for i in range(len(expression)):
        if expression[i].isdigit():
            prePos = i-1
            debug(DEBUG, ('prePos: ', expression[prePos]))
            if expression[prePos] is '-':
                prePrePos = prePos - 1
                # check again to make sure it isn't negative.
                if prePrePos >= 0:
                    if expression[prePrePos] in operations:
                        # basically if a plus then operation come before
                        # a number, then SEND FALSE.
                        print "Please avoid using negative numbers"
                        return invalid
                else:
                    # if prePrePos DOES go into the negatives, that means we
                    # it probably looks like "+x...", which is still in front.
                    print "Please avoid using negative numbers"
                    return invalid                    
    return valid                    
    
def parenthTest(expression):
    
    # call numSeperator to get a proper list of everything
    # then call evaluator, which will use a stack. 
    # and between each parenth. evaluation, it'll call parenthTest to make
    # it's still valid.
    # example: 
# ((3+2)+4) will be sent. it'll take the first parenth. and then the second one
# it sees it will put THAT, then the next num, the next operator, then the 
# next number, and IF the next thing is NOT a right parenthesis, it'll return 
# false. Otherwise, it'll have the '(' location and the ')' location, remove 
# them and everything in between and replace it with the answer from eval.
# then we have (5+4) and do this all over again. If the changed string is 
# just a single number, then we stop and return the number.
    
    valid = True # legibity variable
    invalid = False # legibility variable
    
    parenthCount = 0 # this will keep track of consistencies.
    parenthThreshold = 0
    # gotta test to make sure it begins AND ends with parenthesis
    if expression[0] != '(' or expression[-1] != ')':
        print "Please write a fully parenthesized expression"
        return invalid
    for char in expression:
        if char is '(':
            parenthCount += 1
        elif char is ')':
            parenthCount -= 1
        # after each char, check to make sure it isn't below 0
        if parenthCount < parenthThreshold:
            print "Please write a fully parenthesized expression"
            return invalid
    #after the whole expression is checked, balance should be 0.
    if parenthCount != parenthThreshold:
        print "Please write a fully parenthesized expression"
        return invalid
    else:
        # this is one last failsafe to make sure it's compatible:
        try:
            eval(expression)
        except:
            # if eval fails, it's GG. return False.
            print "Please write a fully parenthesized expression"
            return invalid
    # if all else works, THEN we can go ahead and test to make sure it complies
    # to the formatting standard of (x+x).
    
        
        
        
    return valid
    

                        
    
def numSeperator(expression):
    # put everything into a list, so all other code is simpler.
    expressList = []
    newList = []
    # used to create number from list 
    numString = ''
    i = 0
    
    
    for char in expression:
        expressList.append(char)
    
    # this loop will sort all the proper characters into the right order,
    # so then we can check for the (x+x) format.
    for i in range(len(expressList)):
        if expressList[i].isdigit():
            numString += expressList[i]
        else:
            if len(numString) != 0:
                newList.append(int(numString))
                numString = ''
            newList.append(expressList[i])
    # now that everything is in a list, we can easily iterate through it and
    # change things.
    return newList
            
    
    
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
    
    debug(DEBUG, numSeperator('(1+22+444/1)'))    
#    getInput()
    debug(DEBUG, myStack)

    

if __name__ == '__main__':
    main()