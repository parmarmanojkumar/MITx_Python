# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:50:09 2016

@author: Manojkumar Parmar VirKrupa

@Github Repo : MITx_Python

Modified on : 02/04/2016

Version : 1.0

Remarks:
"""

import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals
pylab.plot(range(1000),tVals)