# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 18:42:34 2016

@author: VirKrupa
"""

bucketSize = 365
numInsertion = 30
def probabilityCollision (bucketSize, numInsertion):
    probCollision = 1.00
    rangeRun = bucketSize -(numInsertion -1)
    for i in range(rangeRun,bucketSize):
        probCollision = probCollision * i/bucketSize
    
    return (1- probCollision)

