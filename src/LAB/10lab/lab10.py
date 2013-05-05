'''
Created on Apr 23, 2013

@author: eliot2
'''
import math as m

def printGreeting():
    print "HELLO! LEtS get some test info!! enter the filename: "
    
def readFile():
    filename = raw_input()
    myFile = open(filename, 'r')
    return myFile

def findMean(myList):
    entries = len(myList)
    total = 0
    for value in myList:
        total += int(value)
    mean = total/entries
    return mean
    
def main():
    myDict = {}
    
    printGreeting()
    myFile = readFile()
    for line in myFile:
        names = line.split()
        myDict[names[0]] = names[1]
    myFile.close()
    myList = []
    myList = myDict.values()
    myList.sort()
    print myDict
    print myList
    mean = findMean(myList)
    print "MEAN: ", mean
    print "MAX: ", myList[-1]
    print "MIN: ", myList[0]
    
    myName = raw_input("Name?? ")
    if myDict.has_key(myName):
        if int(myDict[myName]) < mean:
            print myName, " IS LESSER THAN MEAN"
        elif int(myDict[myName]) > mean:
            print myName, " IS GREATER THAN MEAN"
        else:
            print myName, " IS EXACTLY THE MEAN!"
    else:
        print "NAME NOT IN DICT! NOW QUITTING."
    
if __name__ == '__main__':
    main()