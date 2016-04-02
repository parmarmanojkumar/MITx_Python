# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 14:59:05 2016

@author: Manojkumar Parmar VirKrupa

@Github Repo : MITx_Python

Modified on : 02/04/2016

Version : 1.0

Remarks:
"""

# pylint: disable=invalid-name
import random

class BucketTwoColor(object):
    """
    bucket calss which support replacement drawing and no replacement drawing
    of balls
    """
    def __init__(self, numColorRed, numColorGreen):
        """
        Initialization of bucket with number of red balls and green balls.
        """
        self.bucket = ([0] * numColorRed) + ([1] * numColorGreen)
#        random.shuffle(self.bucket)

    def __str__(self):
        """
        To print current bucket with its status
        """
        numColorGreen = sum(self.bucket)
        numColorRed = len(self.bucket) - numColorGreen
        stringPrint = "Current Status of bucket" + str(self.bucket) + "\n"
        stringPrint += "Statistics : Total - " + str(len(self.bucket)) + " | "
        stringPrint += "Red  :" + str(numColorRed) + " | "
        stringPrint += "Green  :" + str(numColorGreen) + "\n"
        return stringPrint

    def drawBallNoReplacement(self):
        """
        Provides randomly selected ball and removes it from bucket
        """
        val = self.drawBallReplacement()
        self.bucket.remove(val)
        return val

    def drawBallReplacement(self):
        """
        Provides randomly selected ball
        """
        return random.choice(self.bucket)

    def drawBallsSameColor(self, numberDraws, replacementFlag):
        """
        Retunrs true when all drawn balls are of same color

        Raises error when number draws are < 2 or draws are higher than bucket
        size.

        Differentiates between replacement and no replacement type of bucket

        """

        if numberDraws < 2:
            raise ValueError(" NUmber draws must be more than 1")
        if numberDraws > len(self.bucket):
            raise ValueError(" Number of draws are more than bucket size")
        # Based on replacement type function call is made.
        # pylint: disable=unused-variable
        if replacementFlag:
            removedBalls = [self.drawBallReplacement() \
                                for i in range(numberDraws)]
        else:
            removedBalls = [self.drawBallNoReplacement() \
                                for i in range(numberDraws)]
        # pylint: enable=unused-variable
        return (sum(removedBalls) % numberDraws) == 0



def bucketSimulation(numBallsRed, numBallsGreen, numTrials,
                     numSameBalls, replacementFlag):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing numSameBalls balls out of a bucket containing
    numBallsRed red and numBalls green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times
    balls of the same color were drawn in the first numSameBalls draws.
    """
    # capture count of successTrial in given numTrials
    successTrial = 0
    # run for number of trials
    # pylint: disable=unused-variable
    for i in range(numTrials):
        bucket = BucketTwoColor(numBallsRed, numBallsGreen)
        successTrial += int(bucket.drawBallsSameColor(numSameBalls,
                                                      replacementFlag))
    # pylint: enable=unused-variable
    return float(successTrial) / numTrials

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    return bucketSimulation(4, 4, numTrials, 3, True)


# Test cases
trialList = [10000, 10000, 10000, 100000, 100000]
for trails in trialList:
    print "Number of trials : ", trails,
    print "| Success Rate : ",
    print drawing_without_replacement_sim(trails)

