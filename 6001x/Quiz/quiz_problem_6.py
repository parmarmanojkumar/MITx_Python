# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 07:18:35 2016

@author: VirKrupa
"""

listA = [1, 2, 3]
listB = [4, 5, 6]



def flatten(aList):
    result = []
    for entry in aList:
        if hasattr(entry, "__iter__") and not isinstance(entry, basestring):
            result.extend(flatten(entry))
        else:
            result.append(entry)
    return result
        
