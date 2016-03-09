# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 07:18:35 2016

@author: VirKrupa
"""

aString = "ManaM"

lString = len(aString)



def isPalindrome(aString):
    '''
    aString: a string
    Returns True if string is pelindrome
    '''
    if len(aString) <= 1:
        return True
    elif aString[0] == aString[-1] :
        return isPalindrome(aString[1:-1]) and True
    else:
        return False
    