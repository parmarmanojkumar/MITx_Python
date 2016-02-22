# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 08:31:29 2016

@author: mas2cob
"""

class genPrimes1(object):
    def __init__(self):
        self.count = 2
        self.primeVal = [2]
    
    def __str__(self):
        return "Current Number :" + str(self.count)+" ||  List of Prime Number: "+ str(self.primeVal)
    
    def next (self):
        self.count += 1
        for number in self.primeVal:
            if (self.count % number == 0):
                return(None)
        self.primeVal.append(self.count)
        

#a = genPrimes1()
##print(a)
#for i in range(100):
#    a.next()
##print(a)

def genPrimes():
    count = 1
    primeVal = []
    while True :
        gen = False
        count += 1
        for number in primeVal:
            if (count % number == 0):
                gen = True
                break
        if (gen == False) :
            primeVal.append(count)
            yield count

b = genPrimes()

#for n in genPrimes():
#    print n

#primeGenerator = genPrimes()
#print(primeGenerator.next())