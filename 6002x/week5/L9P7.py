# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:44:29 2016

@author: Manojkumar Parmar VirKrupa

@Github Repo :

Modified on :

Version :

Remarks:
"""

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        Edge.__init__(self, src,dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return Edge.__str__(self) + " ("+ str(self.weight)+")"