'''
File:        lab1.py
Author:      Eliot Carney-Seim
Date:        2.12.13
Email:       eliot2@umbc.edu
Section:     10
Description: Hello World!
'''

import os, time

def main():
    
    i = 0
    repeatAmnt = 1
    printSpeed = 0.5
    message = 'Hello World!'
    for i in range(repeatAmnt):
        tempMessage = ''
        for i in range(len(message)):
            os.system('clear')
            tempMessage += message[i]
            print tempMessage
            time.sleep(printSpeed)
    
main()
