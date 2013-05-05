from graphics import *
from time import sleep
'''
File:        hw7.py
Author:      Eliot Carney-Seim
Date:        Apr 7, 2013 11:38:59 PM
Section:     10
Email:       eliot2@umbc.edu
Description: This program is a game where the goal is to move your piece across
a 10x10 board, N, E, W, or S, until it as at the goal location. 
'''


GAME_BOARDER =  450
GAME_ORIGIN = 50
CUBE_LENGTH = 50
BOARDER_SIZE = 50

def printGreeting():

    msg = "Hello User, please follow all instructions! Click to move the " \
           "\nPurple Block towards the yellow block (key) to win! "

    return msg

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

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
# takes the player's new XY position and return True if they are now on the 
# border and False if they are not. 
# Inputs:
# playerX - the horizontal grid location
# playerY - the vertical grid location
# Outputs: n/a
# Returns:
# True if either input is greater than to 350 or less than 0
# , else False is returned.
'''
def offBoard(playerX, playerY):
    # the block is aligned by the topleft corner, so we limit it to 350
    if playerX < GAME_ORIGIN or playerX > GAME_BOARDER:
        return True
    if playerY < GAME_ORIGIN or playerY > GAME_BOARDER:
        return True
    return False

'''
# Name: Eliot Carney-Seim
# Description:
# prints out the grid in lines of a 400x400 pixel screen
# Inputs: win, the screen to blit the game to
# Outputs:
# blits the formatted grid
# Returns: n/a
'''
def drawBoard(win):
    # to construct the lines x,y values, by point 1's x,y and point 2's x,y
    x1, y1 = GAME_ORIGIN, GAME_ORIGIN
    x2, y2 = GAME_ORIGIN, GAME_ORIGIN
    lineList = []
    # print out the vertical lines
    for i in range(8):
        lineList.append(Line(Point(x1, GAME_ORIGIN), Point(x2, GAME_BOARDER)))
        x1 += 50
        x2 += 50

    for i in range(8):
        lineList.append(Line(Point(GAME_ORIGIN , y1), Point(GAME_BOARDER, y2)))
        y1 += 50
        y2 += 50
        
    # create the border
    top = Line(Point(GAME_ORIGIN, GAME_ORIGIN), Point(GAME_BOARDER, \
                                                      GAME_ORIGIN))
    left = Line(Point(GAME_ORIGIN, GAME_ORIGIN), Point(GAME_ORIGIN, \
                                                       GAME_BOARDER))
    bottom = Line(Point(GAME_ORIGIN, GAME_BOARDER), Point(GAME_BOARDER, \
                                                          GAME_BOARDER))
    right = Line(Point(GAME_BOARDER, GAME_ORIGIN), Point(GAME_BOARDER, \
                                                         GAME_BOARDER))

    lineList.append(top)
    lineList.append(bottom)
    lineList.append(right)
    lineList.append(left)
    # draw everything
    for line in lineList:
        line.draw(win)


'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:
# takes the direction the user entered, the original player's X and Y, and 
# returns the updated player's distance X and Y.
# Inputs:
# playerX - the horizontal grid location
# playerY - the vertical grid location
# win - the screen to blit to
# Outputs: n/a
# Returns:
# moveX - the horizontal grid location
# moveY - the vertical grid location
'''
def getMove(win, playerX, playerY):
    validInput = False
    while not(validInput):
        movePoint = win.getMouse()
        if movePoint.y < playerY:
            if movePoint.x > playerX:
                if movePoint.x > playerX + CUBE_LENGTH:
                    # move upright
                    moveX, moveY = 50, -50
                else:
                    # move up
                    moveX, moveY =  0, -50
            else:
                #move diagonal up, left
                moveX, moveY =  -50, -50
        else:
            if movePoint.x < playerX:
                if movePoint.y > playerY + CUBE_LENGTH:
                    # move diagonal down left
                    moveX, moveY =  -50, 50
                else:
                    # move left
                    moveX, moveY =  -50, 0
            elif movePoint.x > playerX + CUBE_LENGTH:
                if movePoint.y > playerY + CUBE_LENGTH:
                    # move diagonal downright
                    moveX, moveY = 50, 50
                else:
                    # move right
                    moveX, moveY = 50, 0
            else:
                # move down
                moveX, moveY = 0, 50
                
        # even if a valid direction is given, setting validInput to true,
        # it'll be set back to false if that input throws us off the board.
        if offBoard(playerX + moveX, playerY + moveY):
            print "Please enter a valid direction."
            validInput = False
        else:
            validInput = True

    return (moveX, moveY)
# CLASSES
# this holds all relevent information and moves the player.
class player(object):
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.rect = Rectangle(Point(xPos, yPos), Point(xPos + 50, yPos + 50))
        self.rect.setFill("purple")

    def move(self, direction):
        self.rect.move(direction[0], direction[1])
        self.xPos += direction[0]
        self.yPos += direction[1]

    def draw(self, win):
        self.rect.draw(win)

def main():

    # construct the screen
    # add 100 so that we have a boarder
    win = GraphWin("hw7.py", GAME_BOARDER+50, GAME_BOARDER+50)
    drawBoard(win)

    greeting = Text(Point(250, 475), printGreeting())
    
    # create and draw our player
    player1 = player(GAME_ORIGIN, GAME_ORIGIN)
    player1.draw(win)
    greeting.draw(win)

    # create and draw our key
    keyPos = Point(250, 250)
    key = Rectangle(keyPos, Point(300, 300))
    key.setFill("yellow")
    key.draw(win)

    # set our play variables
    playing = True
    count = 0
    while playing:
        direction = getMove(win, player1.xPos, player1.yPos)
        player1.move(direction)
        # compare positions to ascertain victory
        if player1.rect.getP1().x == key.getP1().x:
            if player1.rect.getP1().y == key.getP1().y:
                # if all values equal, kill the key and quit the game
                key.undraw()
                greeting.setText("YOU WIN, YOU GOT THE KEY. Now Quitting Game")
                sleep(1)
                playing = False
        count += 1

main()
