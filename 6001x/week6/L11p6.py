# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 21:40:18 2016

@author: VirKrupa
"""

class Queue(object):
    """An Queue is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once.
    It is implemented as FIFO"""
    
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
    
    def insert(self, element):
        """Assumes e is an integer and inserts e into self and sorts it""" 
        self.vals.append(element)
        self.vals.sort()
    
    def remove(self):
        """Pops out element from Queue
           Raises ValueError if queueis is empty"""
        try : 
            return(self.vals.pop())
        except : 
            raise ValueError ()
    
    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


queue = Queue()
queue.insert(5)
queue.insert(6)
print(queue)
print(queue.remove())
queue.insert(7)
queue.remove()
queue.remove()
queue.remove()
            