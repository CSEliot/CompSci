'''
Created on Apr 23, 2013

@author: eliot2
'''

class queue():
    '''
    classdocs
    '''


    def __init__(self):
        self.dict = {}
        
    def enqueue(self, key, thing):
        if self.dict.has_key(key):
            self.dict[key].append(thing)
        else:
            self.dict[key] = [thing]

    def peek(self,key):
        return self.dict[key][0]
    
    def dequeue(self, key):
        return self.dict[key].pop(0)
        