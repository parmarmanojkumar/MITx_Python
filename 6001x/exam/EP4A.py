# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:18:05 2016

@author: VirKrupa
"""




def getSublists(L,n):

    iterateRange = (len(L) - n)+1
    
    returnList = list()
    
    for i in range(iterateRange):
        returnList.append(L[i:i+n])
    
    return returnList
    

L=[10,4,6,8,3,4,5,3,7,9,2]
n = 1
#print getSublists(L,n)
def longestRun(L):
    iterateRange = len(L)
    oldElement = L[0]
    count = 0
    longestCount = None
    for i in range(iterateRange)[1:]:
        if L[i] >= oldElement:
            count = count + 1
            if count >= longestCount:
                longestCount = count
        else:       
            count = 0  
        oldElement = L[i]
    if longestCount == None:
        longestCount = count 
    longestCount += 1
    return longestCount
    
    