# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:48:50 2016

@author: VirKrupa
"""

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5
    
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    else:
        lenL = []
        for element in L:
            lenL.append(len(element))
        return stdDev(lenL)
    


    