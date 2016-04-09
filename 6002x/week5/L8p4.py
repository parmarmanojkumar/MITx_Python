# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:38:53 2016

@author: Manojkumar Parmar VirKrupa

@Github Repo :

Modified on :

Version :

Remarks:
"""


import pylab

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result


def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """
    # Your code here
    N = 3 ** len(items)
    # enumerate the 2**N possible combinations
    i = 0
    while i < N:
        combo1 = []
        combo2 = []
        j = 0
        while j < N:
            # test bit jth of integer i
            tmp = (i / (3 ** j)) % 3
            if tmp == 1:
                combo1.append(items[j])
            elif tmp == 2:
                combo2.append(items[j])
            j += 1
        yield  (combo1 , combo2)
        i += 1

def buildItemsSmall():
    names = ['clock', 'painting', 'radio']
    vals = [175,90,20]
    weights = [10,9,4]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items

def testYieldAllCombos():
    bagTuple = yieldAllCombos(buildItemsSmall())
    maxCount = 0
    countBag = 0
    for aBag in bagTuple:
        countBag+= 1
        for items in aBag:
            print "Start of Bag : ",
            count = 0
            for item in items:
                count += 1
                print item ,"|",
            print "Total Count :" , count
            maxCount = max(maxCount, count)
    print "Max count in bag ", maxCount , "| Item groups in a bag : ", countBag

testYieldAllCombos()