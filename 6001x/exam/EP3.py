# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 08:24:45 2016

@author: VirKrupa
"""

d = {1:10, 2:20, 3:30, 4:30}
d = {4:True, 2:True, 0:True}

def dict_invert(d):
    """
    d: dict
    Returns aninverted dictionary according to the instruction.
    The inverse of a dictionary d is another dictionary whose keys are the 
    unique dictionary values in d . The value for a key in the inverse 
    dictionary is a sorted list of all keys in d that have the same value in d. 
    """
    invDict = dict()
    newKey = None
    for element in d:
        newKey = d[element]
        if invDict.has_key(newKey):
            invDict[newKey].append(element)
            invDict[newKey].sort()
        else:
            invDict[newKey] = [element]
    return invDict.copy()

print dict_invert(d)
    