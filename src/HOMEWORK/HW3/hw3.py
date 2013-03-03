'''
File:        hw3.py
Author:      Eliot Carney-Seim
Date:        2.20.2013
Section:     10
Email:       eliot2@umbc.edu
Description: 

This program will prompt the user to enter an English string and will output 
that string in Pig Latin.

It will look at each space in the string, if the space does not contain a 
letter, it will simply add it to the new string (newStory), if the space 
DOES contain a letter, it will see if that letter is a part of a word. If the 
letter isn't, it will just add the letter and it's adjacent letters/symbols to
the newStory, if it IS a word, it will search for a vowel. If there isn't a 
vowel, it will just add it to the new story. If there IS a vowel, it will pigify 
the word, then add it to the new string. 
It will look at the next space after each word.

Assumptions: 
    No punctuation
    No spaces
    Only letters (though it will work with other characters, not fully)
'''


# ATTN GRADER: EXTRA CREDIT WAS ATTEMPTED

def capCheck(word):
# tests to see if the letter in the word is capitalized. Returns a list of
# the location of all capitalized letters in the word.
    location = -1
    capList = []
    for letter in word:
        location = location + 1
        # if the letter is NOT equal to it's lowercase equivalent.
        if not (letter == letter.lower()):
            capList.append(location)
    return capList

def debug(debugBool, info):

    if (debugBool):
        print "\nDEBUG INFO: ", info
        return True
    return False

def main():

    # CONSTANTS
    VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
    DEBUG = False

    # VARIABLES
    story = ''  # original input from the user
    newStory = ''  # pigified input
    storyPos = -1  # position in the story
    wordPos = -1  # position in the word
    posOriginal = 0  # where the word is found in the story.
    wordPosOriginal = 0  # where the vowel is found in the word.
    movedString = ''  # the consonants before the vowel
    word = ''  # our word that may or may not be modified.
    foundVowel = False  # True if the word had a vowel
    noVowel = False  # True if the tested word is vowel-less.
    added = False  # No need to add the word twice to newStory


    # run
    story = raw_input("Please enter the string that you want to pigify: \n")
    debug(DEBUG, story)

    while storyPos != len(story) - 1:
        debug(DEBUG, 'storyPos starts at {0}'.format(storyPos))
        storyPos = storyPos + 1
        posOriginal = storyPos
        if story[storyPos].isalpha():
            # grab the first letter in the word
            word = story[storyPos]
            debug(DEBUG, 'first letter of word is {0}'.format(word))
            # grab the next letter, if part of the word, and add it to word.
            while (storyPos + 1 < len(story)) and (story[storyPos + 1] != ' '):
                storyPos = storyPos + 1
                word = word + story[storyPos]
            debug(DEBUG, 'Word is ' + word)
            # if the word is indeed an word, test for a vowel
            if(word.isalpha()):
                # test to see if y is the first letter, if true, skip it.
                if word[0] is 'y' or word[0] is 'Y':
                    wordPos = wordPos + 1
                    debug(DEBUG, 'found a Y at {0}'.format(wordPos))
                debug(DEBUG, 'Which is a word.')
                # go through the word till a vowel is found.
                while foundVowel is False and noVowel is False:
                    # for letter in word:
                    # update location in the word so we know where the
                    # vowel was found.
                    wordPos = wordPos + 1
                    # find the first vowel in the word
                    if word[wordPos] in VOWELS:
                        foundVowel = True
                        # recording where we found the vowel
                        debug(DEBUG, 'Vowel @: {0}'.format(wordPos))
                        debug(DEBUG, 'Which is: {0}'.format(word[wordPos]))
                        wordPosOriginal = wordPos
                    # if we get to the end of the word and no vowels are found.
                    if wordPos == len(word) - 1:
                        noVowel = True
            else:
                if added is True:
                    newStory = newStory + word
                    added = True
            if foundVowel and (word.isalpha()):
                # get a list of all the capitalized letters.
                capList = capCheck(word)
                # while the letter is not the first letter in the word.
                # (meaning, the vowel isn't the first letter.
                while wordPos is not 0 :
                    # grab the character behind the vowel/last letter
                    wordPos = wordPos - 1
                    debug(DEBUG, 'Moving: {0}'.format(wordPos))
                    # and put into the movedString (this will be backwards)
                    movedString = movedString + (word[wordPos])
                # once we've reached the beginning of the word in
                # the string, slice out the characters that we are moving
                word = word[wordPosOriginal:]
                # flip the string back in order
                movedString = movedString[::-1]
                debug(DEBUG, 'Word: ' + word + ' + MovedString: ' + movedString)
                # build our new, pigified word.
                word = word + movedString + 'ay'
                # bring everything down to lower, and then upper right at 'loc'.
                word = word.lower()
                debug(DEBUG, 'Word before caps: {0}'.format(word))
                for loc in capList:
                    word = word[:loc] + word[loc].upper() + word[loc + 1:]
                debug(DEBUG, 'Word after caps: {0}'.format(word))
                # add the word to our new story!
                if added is False:
                    newStory = newStory + word
                    added = True
            else:
                if added is False:
                    newStory = newStory + word
                    added = True
            # return variables back for testing the next word.
            foundVowel = False
            noVowel = False
            wordPos = -1
            word = ''
            movedString = ''
            added = False
            capList = []
        else:
            # if the character/word isn't an alphanumeric or part of a word
            debug(DEBUG, 'Adding {0} '.format(story[storyPos]))
            debug(DEBUG, 'from pos: {0}'.format(storyPos))
            newStory = newStory + story[storyPos]
            debug(DEBUG, 'New story:  ' + newStory)
    print 'Your input, in pig-Latin, is: '
    print newStory
main()


