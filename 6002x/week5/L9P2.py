# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:46:55 2016

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
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')'\
            + str(self.dest)

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)



nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

# nodes[0] ABC <-> (ACB,  BAC) |keeping (A, C) constant |
# No repeat
g.addEdge(Edge(nodes[0],nodes[1]))
g.addEdge(Edge(nodes[0],nodes[2]))

# nodes[1] ACB <-> (ABC, CAB) |keeping (A, B) constant |
# ACB-ABC repeat
g.addEdge(Edge(nodes[1],nodes[4]))

# nodes[2] BAC <-> ( BCA, ABC) |keeping (B, C) constant |
# BAC-ABC repeat
g.addEdge(Edge(nodes[2],nodes[3]))

# nodes[3] BCA <-> (CBA, BAC) |keeping (A, B) constant |
# BCA-BAC repeat
g.addEdge(Edge(nodes[3],nodes[5]))

# nodes[4] CAB <-> (ACB, CBA) |keeping (B, C) constant |
# CAB-BAC, repeat
g.addEdge(Edge(nodes[4],nodes[5]))

# nodes[5] CBA <-> (BCA, CAB) |keeping (A, C) constant |
# CBA-BCA, CBA-CAB repeat

print g