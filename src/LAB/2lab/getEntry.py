'''
Created on Mar 26, 2013

@author: eliot2
'''


from graphics import *
from time import sleep
import Tkinter
from Tkinter import Button
from lxml.html.builder import BUTTON
from pydoc import text

def main():
    
    win = GraphWin("DISPLAY", 400, 400)
    win.setCoords(0, 0, 5, 5)
    entry1 = Entry(Point(0,4.5), 25)
    entry2 = Entry(Point(0,3.5), 25)
    entry3 = Entry(Point(0,2.5), 25)    
    entry4 = Entry(Point(0,1.5), 25)
    entry5 = Entry(Point(0,.5), 25)
    entry1.draw(win)
    entry2.draw(win)
    entry3.draw(win)
    entry4.draw(win)
    entry5.draw(win)
    num1 = eval(entry1.getText())
    num2 = eval(entry2.getText())
    num3 = eval(entry3.getText())
    num4 = eval(entry4.getText())
    num5 = eval(entry5.getText())
     
    total = (num1 + num2 + num3 + num4 + num5)/5.0
     
    out = Text(Point(4,4), total)
    
    sleep(10)
    
main()