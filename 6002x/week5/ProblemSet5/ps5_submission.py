# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 11:45:57 2016

@author: Manojkumar Parmar VirKrupa

@Github Repo :

Modified on :

Version :

Remarks:
"""



class WeightedEdge(Edge):
    def __init__(self, src, dest, totDistance, outDistance):
        Edge.__init__(self, src, dest)
        self.totDist = totDistance
        self.outDist = outDistance
    def getTotalDistance(self):
        return self.totDist
    def getOutdoorDistance(self):
        return self.outDist
    def __str__(self):
        return Edge.__str__(self) + " ({0}, {1})".format(self.totDist,self.outDist)

class WeightedDigraph(Digraph):
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        totDist = float(edge.getTotalDistance())
        outDist = float(edge.getOutdoorDistance())
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest , (totDist, outDist)])
    def childrenOf(self, node):
        childList = []
        for entry in self.edges[node]:
            childList.append(entry[0])
        return childList
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2} ({3}, {4})\n'.format(res, k, d[0], d[1][0], d[1][1])
        return res[:-1]

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    ##### Internal Functions Start
    def getPaths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in graph.childrenOf(start):
            if node not in path:
                newpaths = getPaths(graph, node, end, path)
                if newpaths != None:
                    for newpath in newpaths:
                        paths.append(newpath)
        return paths

    def calcPathLength(digraph,aPath):
        totDist = 0.0
        outDist = 0.0
        for idx in xrange(len(aPath)-1):
            nextNode = aPath[idx+1]
            for link in digraph.edges[aPath[idx]]:
                    if link[0] == nextNode:
                        totDist += link[1][0]
                        outDist += link[1][1]
        return totDist, outDist

    def calcPathsDetails(digraph, pathsList):
        pathsDetail = []
        for path in pathsList:
            totDist, outDist = calcPathLength(digraph, path)
            pathsDetail.append([path, totDist, outDist])
        return pathsDetail[:]

    def calcShortestPathWithCriteria(pathsDetailed, \
                                     maxTotalDist, maxDistOutdoors):
        shortestPath = []
        shortestPathVal = float(maxTotalDist)
        for path in pathsDetailed:
            if path[1] <= maxTotalDist and path[2] <= maxDistOutdoors:
                if path[1] < shortestPathVal:
                    shortestPathVal = path[1]
                    shortestPath = path[0]
        if len(shortestPath) == 0:
            return list(), None
        else :
            sPath = []
            for node in shortestPath:
                sPath.append(node.getName())
            return sPath[:], shortestPathVal


    ##### Internal Functions End
    # Step0 : load map | loaded map is availble
    # Step1 : Calcuate all availabe path
    pathsAvailable  = getPaths(digraph, Node(start), Node(end))
    # Step2 : Calculate path distances for available paths
    pathsAvailable = calcPathsDetails(digraph, pathsAvailable)
    # Step3 : Calculate Shortest path meeting criteria for total distance and
    #           outdoor distance
    sPath, sPathVal = calcShortestPathWithCriteria(pathsAvailable,
                                                  maxTotalDist,
                                                  maxDistOutdoors)
    if len(sPath) == 0:
        raise ValueError(" No path available meeting criteria")
    else:
        return sPath
