'''
Created on Apr 23, 2013

@author: eliot2
'''

from Book import book
from Queue import queue

def main():
    
    book1 = book('harper', 'abook', 1, 9)
    book2 = book('haper', 'bbook', 2, 5)
    book3 = book('hooper', 'cbook', 4, 7)
    
    queuer = queue()
    queuer.enqueue('buy', book1)
    queuer.enqueue('buy', book2)
    queuer.enqueue('buy2', book3)
    print queuer.peek('buy').get_all()
    print queuer.peek('buy2').get_all()
    queuer.dequeue('buy')
    queuer.dequeue('buy2')
    print queuer.peek('buy').get_all()
    print queuer.peek('buy2').get_all()

if __name__ == '__main__':
    main()