# lab12.py
# Sue Evans
# 11/18/09

import sys
import string

# getListOfStrings() opens a file, reads each line of the file, strips
# any leading or trailing whitespace, creates a list of the strings,
# closes the file and returns the list of strings
#
# Input:  the name of the file to open
# Output: the list of strings read from the file
def getListOfStrings(filename):

    origList = []
    infile = open(filename, 'r')
    
    for line in infile:
        myStr = string.strip(line)
        origList.append(myStr)

    infile.close()
    return origList

# purgeString() takes a string and makes a new string which has been
# purged of all the non-alphabetic characters.  The purged string is
# in all capitals
#
# Input:  a string
# Output: an all-caps string of letters that were in the string passed in
def purgeString (myStr):

    purged = ''
    
    myStr = string.upper(myStr)

    for ch in myStr:
        if(ch >= 'A' and ch <= 'Z'):
	    purged = purged + ch
    
    return purged

# isPalindrome() determines whether the string passed in is a palindrome.
# This is a recursive function.
#
# Inputs: tempStr, the all-caps, purged string
#         left, the left index
#         right, the right index
# Output: True or False
def isPalindrome (tempStr, left, right):
    test = False
    if left > right:
        return True
#     print left, right
#     print tempStr[left], tempStr[right]
    if tempStr[left] == tempStr[right]:
        test = isPalindrome(tempStr, left+1, right-1)
        
    return test

def main():

    argQ = len(sys.argv)
    if argQ != 2:
        print "WRONG NUMBER OF ARGS: ", 
        print argQ, "Please give one command line arg"
        sys.exit()
    myFile =  sys.argv[1]
    myList = getListOfStrings(myFile)
    palList = []
    print "The palindromes in the file are:"
#     print myList
    for myStr in myList:
#         print myStr
        tempStr = purgeString(myStr)
        if isPalindrome(tempStr, 0, len(tempStr)-1):
            palList.append(myStr)
    
    # call getListOfStrings to get the origList
    for string in palList:
        print string



    # for each of the strings in origList

        # make a tempStr by calling purgeString()
        # tempStr will be in all uppercase with non-letters removed


        # determine if tempStr is a palindrome by calling isPalindrome()

            # if it is, print the original string tempStr was made from



main()

