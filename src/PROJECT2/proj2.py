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

DEBUG = False

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
    # if everything passes, then we send a list of everything in order.
    return numSeperator(expression)

'''                                                                                                                                                                    
# Name: Eliot Carney-Seim                                                                                                             
# Description:
# just runs all the other tests in order to organize code better.
# Inputs: 
# Returns: valid, if all tests are passed - boolean: True
           invalid,  if any of the tests to not pass - boolean: False
'''
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
    if any invalid characters exist, it'll return false
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

'''                                                                                                                                                                    
# Name: Eliot Carney-Seim                                                                                                                                              
# Description:
#     tests to make sure no plus comes between an operator and opperand, 
# in that order.
# Inputs: 
# Returns: valid, if all tests are passed - boolean: True
           invalid,  if any of the tests to not pass - boolean: False
'''
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

'''                                                                                                                                                                    
# Name: Eliot Carney-Seim                                                                                                                                              
# Description:
#     tests to make sure no minus comes between an operator and opperand, 
# in that order.
# Inputs: 
# Returns: valid, if all tests are passed - boolean: True
           invalid,  if any of the tests to not pass - boolean: False
'''
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

'''                                                                                                                                                                    
# Name: Eliot Carney-Seim                                                                                                                                              
# Description:
#     Will test t make sure order is correct, to make sure format is correct
# Inputs: expression - given string
# Returns: valid, if all tests are passed - boolean: True
           invalid,  if any of the tests to not pass - boolean: False
'''
def parenthTest(expression):
    
    valid = True # legibity variable
    invalid = False # legibility variable
    operations = ['+', '-', '*', '/']
    
    
    parenthCount = 0 # this will keep track of consistencies.
    parenthThreshold = 0
    # gotta test to make sure it begins AND ends with parenthesis
    if expression[0] != '(' or expression[-1] != ')':
        debug(DEBUG, 'p1')
        print "Please write a fully parenthesized expression"
        return invalid
    for char in expression:
        if char is '(':
            parenthCount += 1
        elif char is ')':
            parenthCount -= 1
        # after each char, check to make sure it isn't below 0
        if parenthCount < parenthThreshold:
            debug(DEBUG, 'p2')
            print "Please write a fully parenthesized expression"
            return invalid
    #after the whole expression is checked, balance should be 0.
    if parenthCount != parenthThreshold:
        debug(DEBUG, 'p3')
        print "Please write a fully parenthesized expression"
        return invalid
    else:
        # this is one last failsafe to make sure it's compatible:
        try:
            eval(expression)
        except:
            # if eval fails, it's GG. return False.
            debug(DEBUG, 'p4')
            print "Please write a fully parenthesized expression"
            return invalid
    # if all else works, THEN we can go ahead and test to make sure it complies
    # to the formatting standard of (x+x).
    # in order to test this, and make sure that something like (2+3+4) doesn't
    # work, but ((2+3)+4) DOES, we have to use this order: number, operation, ).
    #so get the expression in list form.
    expressList = numSeperator(expression)
    for i in range(len(expressList)):
        if expressList[i] == ')':
            #look at the previous character, which should be a number or a ')'.
            # but if it's a ')', we just skip to below.
            if expressList[i-1].isdigit():
                #then look at the character before that, which should be am
                # operation.
                if not(expressList[i-2] in operations):
                    debug(DEBUG, ('p5', expressList[i-2]))
                    print "Please write a fully parenthesized expression"
                    return invalid
                else:
                    # then, a right parenth. or number is valid to come 
                    # before an operation.
                    if expressList[i-3] is ')':
                        # finally, next should be a number
                        if not(expressList[i-4].isdigit()):
                            debug(DEBUG, 'p6')
                            print "Please write a fully parenthesized expression"
                            return invalid
                    elif expressList[i-3].isdigit():
                        # finally. if it's a number, then next should be a '('
                        if not(expressList[i-4] is '('):
                            debug(DEBUG, 'p7')
                            debug(DEBUG, expressList[i-4])
                            print "Please write a fully parenthesized expression"
                            return invalid
            elif not(expressList[i-1] is ')'):
                # if it isnt' a digit not ')', THAN we can call error.
                debug(DEBUG, 'p8')
                print "Please write a fully parenthesized expression"
                return invalid
    return valid
    

                        
'''
# Name: Eliot Carney-Seim      
# Description:
# takes the string and turns it into a list, numbers seperated right.
# Inputs: expression
# returns: newList - expression converted
'''
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
                newList.append(numString)
                numString = ''
            newList.append(expressList[i])
    # now that everything is in a list, we can easily iterate through it and
    # change things.
    debug(DEBUG, newList)
    return newList
            
    
    
'''                                                                                                                                                                    
# Name: Eliot Carney-Seim                                       
# Description:
#     It should be called from main. It should take in the fully parenthesized 
# expression and evaluate it using a stack
# Inputs: expression - as a LIST of all parts seperated.
# Returns: n/a
'''
def evaluateInfix(expression):
    print '\n\n\n-------Using A Stack To Evaluate Infix------------------- '

    myStack = Stack()
    evalStatement = []
    resulting = '' # this is used to get the evalStatement's results
    i = -1
    operand1 = 0
    operator = 1
    operand2 = 2
    evaluating = True
    
    while evaluating:
        i += 1
        char = expression[i]
        # the ) parenthesis will tell us that it's time to
        if char is ')':
            # add the char ')' so it's legible to the eval() function
            evalStatement.insert(0, char)
            # this is just a loop to do these 4 things, one after another.
            # k will always be 0, then 1, then 2, etc.
            # Once we find the  ')' char, we work backwards, topping the stack
            # of it's members, looking at the top member of the stack without
            # removing it. 
            for k in range(4):
                # get rid of the (x+y) statement, and put it in a list to eval.
                if k is operand1:
                    print '\tPopping operand 1: {0} from the stack'.format(\
                                                                  myStack.top())
                elif k is operator:
                    print '\tPopping operator : {0} from the stack'.format(\
                                                                  myStack.top())
                elif k is operand2:
                    print '\tPopping operand 2: {0} from the stack'.format(\
                                                                  myStack.top())
                else:
                    print '\tPopping {0} from the stack'.format(\
                                                                  myStack.top())

                # add the operations to the list to be eval()'ed
                # THIS is where we remove the item, and add it to the list
                # to be operated on.
                evalStatement.insert(0, myStack.pop())
                
            # check to see if the stack is empty. IF it is, then it will
            # receive the final answer below, so we should discontinue the loop   
            if myStack.isEmpty():
                debug(DEBUG, 'Done Evaluating')
                evaluating = False
            # eval the statement and put it back in the stack    
            debug(DEBUG, ('evaluating: ', evalStatement))
            # this looks complicated, but what it does is map all characters
            # in the eval list to strings, then join them seperated by ""
            # finally, sending that to eval for the answer.
            #example: list = a, b, c becomes string = abc
            resulting = eval(''.join(map(str, evalStatement)))
            print 'Pushing ', resulting, 'into the stack'
            """So if our example problem was (1+(3*4)). The first time, this 
            just found the ')' char after 4, then worked backwards to the '('
            char. then it combined them into a string after removing them
            from the stack, the (3*4) gets added back in as 12"""
            myStack.push(resulting)
            #clear the evalStatement for next run
            evalStatement = []
        else:
            print 'Pushing ', char, 'into the stack'
            myStack.push(char)
    print '\n\nFinal answer is: ', myStack.pop()


'''                                                                                                                                                                    
# Name: Eliot Carney-Seim                                                                                                                                              
# Description:
#     It should be called from main. It should take in the fully parenthesized 
# expression and return it as a postfix expression.
# Inputs: expression -  as a list
# Returns: postFix                                                                                                             
'''
def infixToPostfix(expression):    
    print '\n-------Infix to Postfix--------------------'
    
    postFix = []
    operations = ['+', '-', '*', '/']
    # this is used to show OoOPerations, MATH
    priorityDict = {'(': 0, '+':1,  '-':1, '/':2, '*':2}
    stop = False
    
    myStack = Stack()
    for char in expression:
        if char.isdigit():
            debug(DEBUG, 'Found digit, appending')
            postFix.append(char)
        # use this to get rid of '('
        elif char is '(':
            debug(DEBUG, 'PUSHING ( to stack')
            myStack.push(char)
        elif char in operations:
            debug(DEBUG, 'FOUND OPERATOR')
            stop = False
            # check for ( because it's equivalent to isEmpty
            while not(myStack.isEmpty()) and myStack.top() != '(' and not(stop):
                top = myStack.top()
                debug(DEBUG, (priorityDict.get(char) <= priorityDict.get(top)))
                if priorityDict.get(char) <= priorityDict.get(top):
                    # if the * or  / is higher in priority, then add to postFix
                    debug(DEBUG, 'POPPING from stack to "string"')
                    postFix.append(myStack.pop())
                else:
                    debug(DEBUG, 'STOPPING')
                    stop = True
            if not stop:
                # add the char to the stack! only occurs if the operator
                # in the expression is higher in priority to stack's top.
                debug(DEBUG, 'PUSHING operation to stack')
                myStack.push(char)
        elif char is ')':
            while not(myStack.isEmpty()) and myStack.top() != '(':
                debug(DEBUG, 'POPPING from stack to "string"')
                postFix.append(myStack.pop())
            if myStack.top() == '(':
                # get rid of that pesky left parenth.
                debug(DEBUG, 'Popping left parenth.')
                myStack.pop()
    while not(myStack.isEmpty()):
        # clean the stack
        debug(DEBUG, 'Popping from stack to "String"')
        postFix.append(myStack.pop())
    # turn postfix into a string and return
    print 'postFix:', ' '.join(iter(postFix))
    return postFix
            
'''                                                                                                                                                                    
# Name: Eliot Carney-Seim                                                                                                                                              
# Description:
#     It should be called from main. It should take in the postfix  
# expression and evaluate it using a stack
# Inputs: postFix - the expression converted to postfix as a list
# Returns: n/a                                                                                                                                                
'''
def evaluatePostfix(postfix):
    
    myStack = Stack()
    operations = ['+', '-', '*', '/']
    operand1 = 0
    operand2 = 0
    operator = ''
    
    
    
    for char in postfix:
        if char.isdigit():
            print 'Pushing', char, 'into the stack'
            myStack.push(char)
        elif char in operations:
            # need to pop from the stack twice if we wish to evaluate them
            for i in range(2):
                if i is 0:
                    operand2 = myStack.pop()
                    print '\tPopping operand 2: ', operand2, 'from the stack.'
                if i is 1:
                    operand1 = myStack.pop()
                    print '\tPopping operand 1: ', operand1, 'from the stack'
            # fit everything into a proper format for eval method.
            evalStatement = ''+str(operand1)+char+str(operand2) 
            answer = eval(evalStatement)
            print 'Pushing ', answer, 'into the stack'
            myStack.push(answer)
    print '\n\nFinal answer is: ', myStack.top()
                
def main():
    printgreeting()
    
    expression = getInput()
    evaluateInfix(expression)
    evaluatePostfix(infixToPostfix(expression))

    

main()
