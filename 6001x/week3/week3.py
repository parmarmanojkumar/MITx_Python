# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 08:09:38 2016

@author: VirKrupa
"""

testtup = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here

    newtup = ()
    
    for i in range(0,len(aTup),2):
        newtup = newtup + (aTup[i], )
    return(newtup)


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
    

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
    


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    for element in aDict.values() :
        count += len(element)
    return(count)
    
print howMany(animals)

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    big = -1
    bigkey = None
    for key in aDict.keys():
        if (len(aDict[key]) > big ):
            bigkey = key
            big = len(aDict[key])
    return(bigkey)

print biggest(animals)