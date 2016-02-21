# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:59:43 2016

@author: VirKrupa
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other) :
        """Returns intersection of element in object between self and other """
        intersectEl = intSet()
        for e in self.vals :
            if (other.member(e)):
                intersectEl.insert(e)
        return( intersectEl)
    
    def __len__(self):
        """Returns number of element in self """
        return(len(self.vals))
                
        


a = intSet()
a.insert(5)
a.insert(6)
a.insert(7)
print(a)
print(a.member(3))
print(a.member(5))
a.remove(5)
print(a)
#a.remove(3)
a.insert(3)
print(a)
b = intSet()
b.insert(0)
b.insert(1)
b.insert(4)
print(b)
print(a.intersect(b))

