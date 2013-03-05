'''
File:        /home/eliot2/Documents/Computer Science/Fun/CMSC201/src/HOMEWORK/HW4/hw4.py
Author:      Eliot Leo Carney-Seim 
Date:        Feb 24, 2013 4:06:15 PM
Section:     
Email:       eliot2@umbc.edu
Description: 
    Asks a user for their birth year, month, and day and prints out both their 
    western and Chinese zodiac signs.
Assumptions: 
    The user is born at or after 1900.
    Leap year is non-existent.
'''
import datetime, sys

##########CONSTANTS#############################################################
MONTH_DICT = {'JANUARY': 1, 'FEBRUARY': 2, 'MARCH': 3, 'APRIL': 4, 'MAY': 5,
              'JUNE': 6, 'JULY': 7, 'AUGUST': 8, 'SEPTEMBER': 9, 'OCTOBER': 10,
              'NOVEMBER': 11, 'DECEMBER': 12}
# each number represents a month, the other the total num of days possible.
DAY_DICT = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
            10: 31, 11: 30, 12: 31}

DEBUG = False

# ATTN GRADER: EXTRA CREDIT WAS ATTEMPTED

########METHODS################################################################
def debug(debugBool, info):

    if (debugBool):
        print "\nDEBUG INFO: ", info
        return True
    return False

def cvalidate(vtype, comparator, comparatee=None):
    '''
    # This function takes the given type, and the wanted type, both as a string
    # and an option 3rd input. This function is intended for use with raw_input 
    # is used for any type. If the type matches, it will return the string
    # converted to the type, otherwise False. (can be used simply for convert).
    # for strings, the 3rd input MAY be a string to compare to
    # for number types, the 3rd comparatee MAY be a list of range
    # if the 3rd option is used, it will always return a boolean.
    '''

    valid = False
    if vtype == 'str':
        if comparatee is not None:
            if comparator == comparatee:
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
            temp = float(comparator) #@UnusedVariable
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




def main():

    # #GREETING##
    print "Homework #4 of Lupoli's CMSC201 class. This takes in a user's "
    print "birth date info and uses it to find the user's chinese and zodiac"
    print "signs. from the year 1900 to current. Please follow all instructions"
    print "as literally as possible. Thank you \n"

    getInput = ''
    validated = False
    usrDay = 0
    usrMonth = 0
    usrYear = 0
    currentYear = datetime.date.timetuple(datetime.date.today())[0]
    currentMonth = datetime.date.timetuple(datetime.date.today())[1]
    currentDay = datetime.date.timetuple(datetime.date.today())[2]
    inputMessage = ''
    chinese = ''
    western = ''
    yearTemp = 0

    inputMessage = "\nPlease enter a birth year between the years 1900 and "
    inputMessage = inputMessage + '{0}: \n'.format(currentYear)
    getInput = raw_input(inputMessage)
    # check to see if the year input is correct
    validated = cvalidate('int', getInput, [1900, currentYear])
    # if it IS a boolean, and IS in the proper range, then convert to int.
    if validated:
        getInput = int(getInput)
    else:
        raise UserWarning, "Invalid birth year given, please re-launch."
        sys.exit(UserWarning)
    usrYear = getInput
    validated = False



    inputMessage = "Please enter a birth month: as a word or number\n"
    getInput = raw_input(inputMessage)
    # if the user gave us a month number, simply verify that it is possible
    if getInput.isdigit():
        # if the person was born in the same year, meaning a limit on the
        # possible months since the year isn't over yet.
        if usrYear == currentYear:
            validated = cvalidate('int', getInput, [1, currentMonth])
        else:
            # if the year has passed, all months are possible.
            validated = cvalidate('int', getInput, [1, 12])
    else:
        # if the user gave us a name, we must convert it to the number
        # then do the same as above
        getInput = getInput.upper()
        if getInput in MONTH_DICT:
            # the name becomes the number version
            getInput = MONTH_DICT[getInput]
            debug(DEBUG, (usrYear, currentYear))
            if usrYear == currentYear:
                validated = cvalidate('int', getInput, [1, currentMonth])
            else:
                # if the year has passed, all months are possible.
                validated = cvalidate('int', getInput, [1, 12])
    if validated:
        getInput = int(getInput)
    else:
        raise UserWarning, "Invalid birth month given, please re-launch."
        sys.exit(UserWarning)
    usrMonth = getInput





    inputMessage = "\nPlease enter a birth day between the days 1 and "
    inputMessage = inputMessage + '{0}: \n'.format(DAY_DICT[usrMonth])
    getInput = raw_input(inputMessage)
    # check to see if the year input is correct
    validated = cvalidate('int', getInput, (1, DAY_DICT[usrMonth]))
    # if it IS a boolean, and IS in the proper range, then convert to int.
    if validated:
        getInput = int(getInput)
    else:
        raise UserWarning, "Invalid birth day given, please re-launch."
        sys.exit(UserWarning)
    usrDay = getInput

    #######Beginning Massive if-else testing for WESTERN############
    debug(DEBUG, (usrYear, usrMonth, usrDay))

    if usrMonth == 1:
        if usrDay >=21:
            western = 'Aquarius'
        else:
            western = 'Capricorn'
    elif usrMonth == 2:
        if usrDay >= 20:
            western = 'Pisces'
        else:
            western = 'Aquarius'
    elif usrMonth == 3:
        if usrDay >= 21:
            western = 'Aries'
        else:
            western = 'Pisces'
    elif usrMonth == 4:
        if usrDay >= 21:
            western = 'Taurus'
        else:
            western = 'Aries'
    elif usrMonth == 5:
        if usrDay >= 22:
            western = 'Gemini'
        else:
            western = 'Taurus'
    elif usrMonth == 6:
        if usrDay >= 22:
            western = 'Cancer'
        else:
            western = 'Gemini'    
    elif usrMonth == 7:
        if usrDay >= 23:
            western = 'Leo'
        else:
            western = 'Cancer'
    elif usrMonth == 8:
        if usrDay >= 23:
            western = 'Virgo'
        else:
            western = 'Leo'
    elif usrMonth == 9:
        if usrDay >= 24:
            western = 'Libra'
        else:
            western = 'Virgo'
    elif usrMonth == 10:
        if usrDay >= 24:
            western = 'Scorpio'
        else:
            western = 'Libra'
    elif usrMonth == 11:
        if usrDay >= 23:
            western = 'Sagittarius'
        else:
            western = 'Scorpio'
    elif usrMonth == 12:
        if usrDay >= 22:
            western = 'Capricorn'
        else:
            western = 'Sagittarius'
                    
    debug(DEBUG, western)
    
    #######Beginning Massive if-else testing for EASTERN############

    # if user is born in january, then make a fake birthyear to move
    # the year back one animal.
    if usrMonth == 1:
        yearTemp = usrYear - 1
        debug(DEBUG, (usrYear, yearTemp))
    else:
        yearTemp = usrYear
    debug(DEBUG, yearTemp)
    # the remainder will determine which sign you're a part of
    yearTemp = yearTemp % 12
    debug(DEBUG, yearTemp)
    
    # we start with 4, because 1900%12 = 4
    if yearTemp == 4:
        chinese = 'Rat'
    elif yearTemp == 5:
        chinese = 'Ox'
    elif yearTemp == 6:
        chinese = 'Tiger'
    elif yearTemp == 7:
        chinese = 'Rabbit'
    elif yearTemp == 8:
        chinese = 'Dragon'
    elif yearTemp == 9:
        chinese = 'Snake'
    elif yearTemp == 10:
        chinese = 'Horse'
    elif yearTemp == 11:
        chinese = 'Sheep'
    elif yearTemp == 0:
        chinese = 'Monkey'
    elif yearTemp == 1:
        chinese = 'Rooster'
    elif yearTemp == 2:
        chinese = 'Dog'
    elif yearTemp == 3:
        chinese = 'Pig'
        
    debug(DEBUG, chinese)
    
    print 'Given the birthdate: {0}:{1}:{2}'.format(usrYear, usrMonth, usrDay)
    print 'Your Western Zodiac is: %s' % western
    print 'And your Eastern Zodiac is: %s' % chinese    
main()
