###############################################################################
'''
File:         hw1.py
Author:       Eliot Carney-Seim
Date:         2.12.13
Section:
E-mail:       eliot2@umbc.edu
Description: 

'''

def main():

    #Initiate AAAAALLLLL the values.
    odometerInit = 0.0
    odometerFin = 0.0
    gallonsUsed = 0.0
    gallonCost = 0.0
    mileage = 0.0
    costPerMile = 0.0
    totalMiles = 0.0


    print "Hello World, this program will compute the gas mileage of a car!"
    print "Please follow the instructions carefully, failure is not an option"

    #Grab the user inputs.
    print "Please enter the initial odometer reading, and then the final: " 
    odometerInit = input() + 0.0
    odometerFin = input() + 0.0
    print "Please enter the number of gallons used and the cost/gallon: "
    gallonsUsed = input() + 0.0
    gallonCost = input() + 0.0
    
    #calculate necessary values
    totalMiles = (odometerFin - odometerInit)
    mileage = (totalMiles / gallonsUsed)
    costPerMile = (mileage * gallonCost)

    print "Results:"
    print "Total miles driven: {0:0.2f}".format(totalMiles)
    print "  Miles per Gallon: {0:0.2f}".format(mileage)
    print "     Cost per Mile: {0:0.2f}".format(costPerMile)



main()
