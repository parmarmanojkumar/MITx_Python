# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 20:08:51 2016

@author: VirKrupa
"""

import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(0)
    return random.randrange(10,21,2)

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10,21,2)
