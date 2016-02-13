# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 07:18:35 2016

@author: VirKrupa
"""

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    #newL = [entry for entry in L if f(entry)]
#    for entry in L :
#        if f(entry) :
#            newL.append(entry)
    L[:] = [entry for entry in L if f(entry)]
    return(len(L))
            

#run_satisfiesF(L, satisfiesF)

def f(s):
    return 'a' in s

L = ['a', 'b', 'a']
print satisfiesF(L)
print L


    
