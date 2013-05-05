'''
File:        hw6.py
Author:      Eliot Carney-Seim
Date:        Mar 22, 2013 11:38:59 PM
Section:     10
Email:       eliot2@umbc.edu
Description: This program is a game where the goal is to move your piece across
a 10x10 board, N, E, W, or S, until it as at the goal location. 
'''

DEBUG = False
MAX_LEN = 9
MIN_LEN = 0

# CLASSES
# this class is a simple containter object to keep some variables organized.
class startPos(object):
    
    def __init__(self):
        self.pX = 2
        self.pY = 4
        self.kX = 3
        self.kY = 6
        

# FUNCTIONS
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:                                                                                                                                                          
# If the global variable is set to True, all given info will be printed.                                                                                                
# Inputs:                                                                                                                                                               
# debugBool - Boolean: To determine if info should be printed.                                                                                                          
# info - Printable object: Will be printed alongside the string "DEBUG INFO: "                                                                                          
# Outputs:                                                                                                                                                              
# "Debug Info <info>"                                                                                                                                                   
# Returns:                                                                                                                                                              
# If printing: True                                                                                                                                                     
$ If not printing: False                                                                                                                                                
'''
def debug(debugBool, info):

    if (debugBool):
        print "\nDEBUG INFO: ", info
        return True
    return False
pass


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
$ If comparatee:  True or False                                                                                                                                         
'''
def cvalidate(vtype, comparator, comparatee=None):
    '''
    # This function takes the given type, and the wanted type, both as a string
    # and an option 3rd input. This function is intended for use with raw_input 
    # is used for any type. If the type matches, it will return the string
    # converted to the type, otherwise False. (can be used simply for convert).
    # for strings, the 3rd input MAY be a string/list to compare to.
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

    print "Hello User, please follow all instructions! The program does the\n" \
    " following: This program will generate a game for the player. Move "\
    " according to the cardinal directions, and get to the key to win, you may"\
    " not move on the border."

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
# takes the player's new XY position and return True if they are now on the 
# border and False if they are not. 
# Inputs:
# pX - the horizontal grid location
# pY - the vertical grid location
# Outputs: n/a
# Returns:
# True if either input is equal to 9 or 0, else False is returned.
'''
def offBoard(pX, pY):
    if pX == MAX_LEN or pX == MIN_LEN:
        return True
    elif pY == MAX_LEN or pY ==MIN_LEN:
        return True
    return False

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
# takes the direction the user entered, the original player's X and Y, and 
# returns the updated player's X and Y.
# Inputs:
# playerX - the horizontal grid location
# playerY - the vertical grid location
# direction - string of the given cardinal direction
# Outputs: n/a
# Returns:
# playerX - the horizontal grid location
# playerY - the vertical grid location
# changed playerX and playerY based on direction
'''
def updatePosition(direction, playerX, playerY):
    OrigPos = (playerX, playerY)
    # north and south are inverted, due to how comp grids work
    if direction == 'north':
        playerY -= 1
    elif direction == 'south':
        playerY += 1
    elif direction == 'west':
        playerX -= 1
    elif direction == 'east':
        playerX += 1
    else:
        debug(DEBUG, ('NO DIRECTION /WRONG: ', direction))
    # if the move is on the boarder, return the unchanged, past location
    if offBoard(playerX, playerY):
        print "Sorry, you can't move onto the boarder."
        return OrigPos
    return (playerX, playerY)
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:                                                                                                                                                          
# returns True if the player reached the key and False if not.                                                                                               
# Inputs:                                                                                                                                                               
# playerX - the horizontal grid location
# playerY - the vertical grid location
# keyX - the horizontal grid location for the KEY
# keyY - the vertical grid location for the KEY                                                                       
# Outputs: n/a
# Returns:
# A boolean, for if KeyX and KeyY are equal to PlayerX and PlayerY.
'''
def reachedKey(playerX, playerY, keyX, keyY):
    if playerX == keyX and playerY == keyY:
        return True
    return False
'''
# Name: Eliot Carney-Seim
# Description:
# prints out the grid after formatting it correctly
# Inputs: 
# playerX - the horizontal grid location
# playerY - the vertical grid location
# keyX - the horizontal grid location for the KEY
# keyY - the vertical grid location for the KEY
# Outputs:
# prints out the formatted grid
# Returns: n/a
'''
def printBoard(playerX, playerY, keyX, keyY):
    # recreate a basic keyboard each calling
    gameboard = [['_','_','_','_','_','_','_','_','_','_\n'],\
                 ['|','.','.','.','.','.','.','.','.','|\n'],\
                 ['|','.','.','.','.','.','.','.','.','|\n'],\
                 ['|','.','.','.','.','.','.','.','.','|\n'],\
                 ['|','.','.','.','.','.','.','.','.','|\n'],\
                 ['|','.','.','.','.','.','.','.','.','|\n'],\
                 ['|','.','.','.','.','.','.','.','.','|\n'],\
                 ['|','.','.','.','.','.','.','.','.','|\n'],\
                 ['|','.','.','.','.','.','.','.','.','|\n'],\
                 ['_','_','_','_','_','_','_','_','_','_\n']]
    # the x and Y have to be swapped to format with the list
    tempLocPlayer = (playerY, playerX)
    tempLocKey = (keyY, keyX)
    
    # grab the row from which the player resides
    #tempStr = gameboard[tempLocPlayer[0]]
    gameboard[tempLocKey[0]][tempLocKey[1]] = 'K'    
    gameboard[tempLocPlayer[0]][tempLocPlayer[1]] = 'P'
    for i in range(len(gameboard)):
        for j in gameboard[i]:
            print j,


'''
# Name: Eliot Carney-Seim
# Description:
# will keep asking until user gives us input equal to something in allValids
# Inputs: User enters playerInput, to be tested for validity
# Outputs: Asks for user input
# Returns: 
# playerInput - a valid input       
'''
def getInput():

    # sent to the validating function, will return false if has not validInput    
    allValids = ('west', 'north', 'south', 'east')
    playerInput = ''
    validInput = False
    while not(validInput):
        playerInput  = raw_input('Please type in North, South, East, or West')
        playerInput = playerInput.lower()
        validInput  = cvalidate('str', playerInput, allValids)
        if not(validInput):
            print 'Please enter either: "North", "South", "East", or "West"'
        debug(DEBUG, validInput)
    return playerInput

def main():
    
    
    # this class is just an container for easily organizing specific code
    game = startPos()
    printGreeting()
    
    # set the player and key starting positions
    playerPos = (game.pX, game.pY)
    keyPos = (game.kX, game.kY)
    printBoard(playerPos[0], playerPos[1], keyPos[0], keyPos[1])
    while not(reachedKey(playerPos[0], playerPos[1], keyPos[0], keyPos[1])):
        # get the direction that we want from the player.
        playerInput = getInput()
        playerPos = updatePosition(playerInput, playerPos[0], playerPos[1])
        debug(DEBUG, playerPos)
        printBoard(playerPos[0], playerPos[1], keyPos[0], keyPos[1])
    print "YOU FOUND THE KEY!!"

main()
    