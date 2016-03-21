# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:24:23 2016

@author: VirKrupa
"""
import random

def singleTrial(noReplacement = True):
    """
    Function provides single trial for choosing 3 balls from bucket of 6 balls.
    In bucket 3 balls are of green and 3 balls are of red.
    0 represents green and 1 represents red

    returns bucket with randomised ball arrangement

    """
    #Initializes bucket with balls and shuffles them.
    bucket = [0,0,0,1,1,1]
    random.shuffle(bucket)
    trial= 0
    # Simulate 3 pick from bucket
    for i in range(3):
        # Choose randomly a ball
        ball = random.choice(bucket)
        # Remove ball from bucket if no replacement mechanism
        if noReplacement :
            bucket.remove(ball)
        # Add up a score of ball
        trial += ball
    # If all 3 ball are of same color then trial can either be 0 or 3
    # Modulus operation checks for count 0 or 3 and returns sucessful trial
    return (trial % 3 == 0)


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # keeps track of successfull  trial count
    trialSuccessfull = 0.0
    for i in range(numTrials):
        if singleTrial():
            trialSuccessfull += 1

    return trialSuccessfull/numTrials

# Test to run simulation 10 times with 5000 trials
def testSimulation(run = 10 , trialCount = 5000):
    testResult=[]
    for i in range(run):
        testResult.append(noReplacementSimulation(trialCount))
    print "Max Probability :", max(testResult)," | Min Probability :",
    print min(testResult), " | Mean Probability:", sum(testResult)/run