'''
File:        hw2.py
Author:      Eliot Carney-Seim
Date:        2.13.2013
Section:     10
Email:       eliot2@umbc.edu
Description: Lets the user enter four quarterly sales figures for two divisions
of a company in the order shown below. Once the figures are entered, the 
program will display the following data for each quarter:

1.A list of the sales figures by division
2.The total sales for the quarter 
3.The average sales for both divisions that quarter
'''

def main():
    
    #Greeting
    print "Welcome to Homework 2, Please follow all the instructions!"
    
    #Initialize variables
    qrtlySalesDiv1 = []
    qrtlySalesDiv2 = []
    reportsPerYear = 4
    reportRequest  = "Please enter the total sales for Quarter: {0}"
    reportTemp = 0.0


    #grab the reports for each quarter and append them to a string.
    print "For Division Number 1. . ."
    for i in range(reportsPerYear):
        print reportRequest.format(i+1)
        reportTemp = input()
        qrtlySalesDiv1.append(reportTemp)

    #repeat the same process for division number 2.
    print "For Division Number 2. . ."
    for i in range(reportsPerYear):
        print reportRequest.format(i+1)
        reportTemp = input()
        qrtlySalesDiv2.append(reportTemp)


    #print out all the required information
    #first, print out the sales per quarter. . .
    print "Sales per quarter for Division 1: "
    for i in range(reportsPerYear):
        print "\t\t       Quarter {0}: {1}".format(i+1, qrtlySalesDiv1[i])
        
    print "Sales per quarter for Division 2: "
    for i in range(reportsPerYear):
        print "\t\t       Quarter {0}: {1}".format(i+1, qrtlySalesDiv2[i])

    #print out the total sales after adding each parallel report.
    print "          Total Sales by Quarter: "
    for i in range(reportsPerYear):
        print "\t\t       Quarter {0}: {1}".format(i+1,
                                                   qrtlySalesDiv1[i] +
                                                   qrtlySalesDiv2[i])
    #print out the average sales after halving the sum of 2 reports.
    print "       Average Sales per Quarter: "
    for i in range(reportsPerYear):
        print "\t\t       Quarter {0}: {1}".format(i+1,
                           (qrtlySalesDiv1[i] +qrtlySalesDiv2[i]) / 2.0)

main()
    
