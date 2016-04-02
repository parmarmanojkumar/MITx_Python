# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:03:30 2016

@author: Manojkumar Parmar VirKrupa

@Github Repo : MITx_Python

Modified on : 02/04/2016

Version : 1.0

Remarks:
"""

# pylint: disable=invalid-name
import random
import pylab
# You are given this function
def getMeanAndStd(X):
    """
    returns calculated meand and standard deviation on list X
    """
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
# pylint: disable=R0903
class Die(object):
    """
    Die class
    """
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]

    def roll(self):
        """ returns a single roll value of dice."""
        return random.choice(self.possibleVals)
# pylint: enable=R0903
# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated
        labels for the x and y axis
      - If title is provided by caller, puts that title on the figure and
        otherwise does not title the figure
    """
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if not title is  None:
        pylab.title(title)
    pylab.show()
    return None


# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longRun = []

    while numTrials > 0:
        oldElement = die.roll()
        locCount = 1
        gloCount = 1
        numRollTrial = numRolls
        while numRollTrial > 1:
            element = die.roll()
            if oldElement == element:
                locCount += 1
            else:
                locCount = 1
            gloCount = max(gloCount, locCount)
            oldElement = element
            numRollTrial = numRollTrial - 1
        longRun.append(gloCount)
        numTrials = numTrials - 1

    makeHistogram(longRun, 10, "Bins", "# trials")
    # pylint: disable=unused-variable
    mean, std = getMeanAndStd(longRun)
    # pylint: disable=unused-variable
    return mean


# test case implementation 1
#makeHistogram([], 1, "A", "B", "C")
#makeHistogram([1], 4, "Aa", "Bb", "Cc")
#makeHistogram([1,2], 4, "Aaa", "Bbb")
#makeHistogram([1,2,5,6,9,10], 4,"Aaaa", "Bbbb", "Cccc")
#makeHistogram([21,20,19,1,2,2,2,5,6,6,9,10], 5, "Aaaaa", "Bbbbb", "Ccccc")

# test case implementation 2
#print getAverage(Die([1]), 10, 1000)
#print getAverage(Die([1,1]), 10, 1000)
#print getAverage(Die([1,2,3,4,5,6]), 50, 1000)
#print getAverage(Die([1,2,3,4,5,6,6,6,7]), 50, 1000)
#print getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000)
#print getAverage(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 500, 10000)
