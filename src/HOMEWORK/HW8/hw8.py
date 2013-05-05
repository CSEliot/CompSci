'''
File:        hw8.py
Author:      Eliot Carney-Seim
Date:        Apr 13, 2013 11:38:59 PM
Section:     10
Email:       eliot2@umbc.edu
Description: 
The program picks a word (from a file) and displays it with underscores 
replacing the letters. The user tries to guess the word by guessing one letter
at a time. The user loses if they guess too many incorrect letters. For your 
program, set the maximum number of incorrect guesses to 4.
'''

import random as r


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

def printGreeting():
    message = "Hello, this program runs a game of hangman. Please follow all\n"\
              " Instructions, a random word will be taken from the words.txt\n"\
              " file. You will be asked to type in a single letter, with 4 \n"\
              " incorrect guesses before you lose and get hung. Enjoy!\n"
    print message
    return None

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description:                                                                                                                                                          
# Takes the name of the file to read, reads in the words from the file into a 
# list, and returns the list of words. 
# Inputs:
# filename - name of the file to be read in
# Returns:
# words -  a list of all the words from the file                                                                                                                                                              
'''
def readWords(filename):
              
    wordFile = open(filename, 'r')
    # return a string of the file, then split for each word.
    wordList = wordFile.read().split()
    return wordList

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description: Takes the list of words, calls getRandomWord(), and loops until 
               the game is either lost or won.
# Inputs: wordList - list of words given from words.txt
# Returns: n/a
'''
def playGame(wordList): 
    
    gameDone = False
    numMissedLetters = 4
    correctLetters = []
    allGuessedLetters = []
    guess = ''
    
    secretWord = getRandomWord(wordList)
    secretWord = secretWord.lower()

    while not gameDone:
        displayTurn(numMissedLetters, correctLetters, secretWord)
        guess = getGuess(allGuessedLetters)
        guess = guess.lower()
        allGuessedLetters.append(guess)
        if guess in secretWord:
            correctLetters.append(guess)
        else:
            numMissedLetters -= 1

        gameDone = wonGame(correctLetters, secretWord)
        gameDone = lostGame(numMissedLetters)
        
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description: Takes the list of words, randomly chooses a word 
               (using Python random library), and returns the secret word.
# Inputs: wordList - list of words given from words.txt
# Returns: secretWord
'''
def getRandomWord(wordList): 
    secretWord = r.randint(0, len(wordList)-1)
    return wordList[secretWord]
    
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description: Takes the number of incorrect guesses, the list of correct 
# guesses, and the secret word. Displays the secret word, with correctly guessed
# letters visible and the other letters "hidden" with an underscore, and display
# the amount of incorrect guesses left.
# Inputs: 
# numMissedLetters - the number of missed letters
# correctLetters - the list of correctly chosen letters
# secretWord - the word that player is trying to guess.
# Returns: n/a
'''
def displayTurn(numMissedLetters, correctLetters, secretWord):
    
    #printing out the secret word
    for letter in secretWord:
        if letter in correctLetters:
            print letter,
        else:
            print "_",
    print "Incorrect guesses left: ", numMissedLetters, '\n'
    
    return None

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description: Takes a list of all the guessed letters 
(both correct and incorrect). Gets a letter input from the user, checking 
if it is valid, looping until a valid guess has been made, and returns the 
guessed letter.
# Inputs:
# allGuessedLetters - all the letters guessed so far
# Returns: guessedLetter - letter guessed by player
'''
def getGuess(allGuessedLetters):
    validInput = False
    while validInput ==  False:
        guessed = raw_input("Guess a letter: ")
        #make sure the user only enters one letter
        if len(guessed) == 1:
            # send cvalidate the list of guessed letters, if it returns true
            # that means the guessed letter IS in the guessed List, so input is 
            # NOT valid.
            validInput = not(cvalidate('str', guessed, allGuessedLetters))
        if not(validInput):
            print "Please enter a letter not yet guessed"
    return guessed

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description: Takes the list of correct guesses and the secret word, returns
# True if the game has been won and False if not.
# Inputs:
# correctLetters - all letters that have been guessed correctly
# secretWord -  the word that player is trying to guess.
# secretWord - 
# Returns: T/F depending on if win condition is met.
'''
def wonGame(correctLetters, secretWord): 
    #for each letter, check to see if it's in the string secretWord, if ALL
    # true, WIN!!
    # this contains all booleans, if all is True, then WIN!
    winList = []
    for letter in correctLetters:
        if letter in secretWord:
            winList.append(True)
        else:
            winList.append(False)
    if False in winList:
        return False
    else:
        print "YOU WIN!!!"
        return True
'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description: Takes the number of incorrect guesses, return True if the game
has been lost (too many bad guesses) and False if not.    
# Inputs:
# numMissedLetters - list of all letters chosen incorrectly
# Returns: T/F depending on if the missed letters amount matches the lose cond.
'''
def lostGame(numMissedLetters):
    getHungNum = 4
    if numMissedLetters == getHungNum:
        print "YOU LOST. . . wow. . . "
        return True
    else:
        return False  

'''                                                                                                                                                                     
# Name: Eliot Carney-Seim                                                                                                                                               
# Description: Prompts the user if they want to play again. 
# Returns True if yes and False if no.   
# Inputs:
# Returns: T/F depending on if the user inputs yes or no..
'''
def playAgain(): 
    validInput = False
    validAnswers = ['yes', 'no', 'n', 'y']
    while not(validInput):
        print "Please enter yes, no, y or n. . . \n"
        playerResponse = raw_input("Would you like to play again?")
        playerResponse = playerResponse.lower()
        validInput = cvalidate('str', playerResponse, validAnswers)
    if cvalidate('str', playerResponse[0], 'n'):
        return False
    else:
        return True
        
        
        
        
def main():
    
    printGreeting()

    words = readWords('words.txt')
    while playAgain():
        playGame(words)



main()
        
    