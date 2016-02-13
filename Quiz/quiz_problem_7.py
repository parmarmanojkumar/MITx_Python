# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 07:18:35 2016

@author: VirKrupa
"""

listA = [1, 2, 3]
listB = [4, 5, 6]

def f(a,b):
    return (a > b)


d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    difference ={}
    
    for akey in d1.keys() :
        if akey in d2.keys():
            intersect[akey] = f(d1[akey], d2[akey])
        else:
            difference[akey] = d1[akey]
    
    for akey in d2.keys():
        if not akey in d1.keys():
            difference[akey] = d2[akey]
            
    ret_tupple = (intersect, difference)
    return ret_tupple



    
