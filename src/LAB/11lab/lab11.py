'''
Created on Apr 30, 2013

@author: eliot2
'''
import random
import time



# binarySearch() performs a binary search for an myInt in a list
# Inputs: myList, the list to search
#         myInt, the myInt to search for
# Output: the index of myInt in the list, or -1 if not found
def binarysearch(myList, myInt):

    low = 0
    high = len(myList) - 1
    while low <= high:
        mid = (low + high) / 2

        # if found return the index
        if myInt == myList[mid]:
            return myList.index(myInt)

        # if myInt is in the 2nd half of the list
        elif myInt > myList[mid]:
            low = mid+1

        # if myInt is in the 1st half of the list
        else:
            high = mid-1

    # myInt was not in list
    return -1

def linearSearch(myList, myInt):
    for i in range(len(myList)):
        if i == myInt:
            return myList.index(myInt)
    return -1

def main():
    
    searchAmt = input('search amt: ')
    myList = []
    for i in range(1000):
        myList.append(i)
    print myList
    random.shuffle(myList)
    
    print myList

    t0 = time.time()
    for i in range(searchAmt):
        myInt = random.randint(0, 999)
        linearSearch(myList, myInt)
    t1 = time.time()
    print "Linear search time: ", t1-t0
    
    t0 = time.time()
    myList.sort()
    for i in range(searchAmt):
        myInt = random.randint(0, 999)
        binarysearch(myList, myInt)
    t1 = time.time()
    print "Binary search time: ", t1-t0
    
    
    
    
if __name__ == '__main__':
    main()