# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 07:18:35 2016

@author: VirKrupa
"""

listA = [1, 2, 3]
listB = [4, 5, 6]



def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    
    Returns dot product of both lists
    '''
    if listA == [] :
        return 0
    else:
        return (dotProduct(listA[1:], listB[1:]) + (listA[0] * listB[0]))

