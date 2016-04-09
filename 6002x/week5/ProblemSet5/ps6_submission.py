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


#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

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
    stack = []
    stack.append([[Node(start)], (0.0,0.0)])
    sDist = maxTotalDist + 1.0
    sPath = []
    totalDist = 0.0
    outdoorsDist = 0.0
    nEnd = Node(end)

    while len(stack) != 0:
        popEntry = stack.pop()
        path = popEntry[0]
        curNode = path[-1]
        for destNode, (nodeTotDist, nodeOutDist) in digraph.edges[curNode]:
            totalDist = popEntry[1][0]
            outdoorsDist = popEntry[1][1]
            if destNode not in path :
                newPath = path + [destNode]
                totalDist += nodeTotDist
                outdoorsDist += nodeOutDist
                criteria = (totalDist > sDist) or (totalDist > maxTotalDist) or (outdoorsDist > maxDistOutdoors)
                if criteria :
                    continue
                stack.append([newPath, (totalDist, outdoorsDist)])
                if destNode == nEnd:
                    sPath = newPath
                    sDist = totalDist

    if len(sPath) == 0:
        raise ValueError(" No path available meeting criteria")
    else:
        shortestPath = []
        for node in sPath:
            shortestPath.append(node.getName())
        return shortestPath[:]

