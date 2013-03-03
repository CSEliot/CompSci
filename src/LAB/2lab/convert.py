# File:        convert.py
# Written by:  Patti Ordonez
# Date:        5/?/09
# Lab Section: 03
# UMBC email:  ordopa1@umbc.edu
# Description: This program converts degrees in celsius to 
#           degrees in fahrenheit.  

def main():

    degC = input("What is the Celsius temperature ? ")

    degF = (9.0 / 5.0) * degC + 32

    print "The temperature is ", degF, " degrees in fahrenheit"
main()
