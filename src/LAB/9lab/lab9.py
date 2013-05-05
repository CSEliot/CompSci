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
# some constants
MIN_YEAR = 1900
MAX_YEAR = 2500
 
SUNDAY = 0
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6

def printGreeting():
    print "PRINTING A CALENDAR!! Follow the instructions please thank you.    "

def getValidInt(message, min_year, max_year):
    print message 
    # start with an illegal value to get into the loop
    number = -1
    while number < 0:
        number = input("Enter a positive number : ")
    return number

def printMonth(month, year):
    monthDict = {1: 'January', 2:'February', 3:"March", 4:'April', 5:'May', 
                 6: 'June', 7:'July', 8:'August', 9:'September', 10:'October',
                 11:'November', 12:'December'}
    days = "   SU    M     T     W     TH    F    SA"
    day = 0
    weekday = 3
    print "              {0} {1}".format(monthDict[month], year)
    print days
    print "                 ",
    while day < 26:
        while weekday != 7:
            weekday += 1
            day += 1
            if day < 32:
                if day < 10:
                    print "   0{0}".format(day),
                else:
                    print "   {0}".format(day),
        weekday = 0
        print ""
    None

def printCalendar(year):
    month = 0
    while month < 12:
        month += 1
        printMonth(month, year)
    return None

def main():
 
    printGreeting()
    valid = False

    while valid == False:
        year = getValidInt("Which year would you like? ", MIN_YEAR, MAX_YEAR )
        valid = cvalidate('int', year, (MIN_YEAR, MAX_YEAR))
    printCalendar(year)
 
main()