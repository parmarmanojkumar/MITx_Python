# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)



class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
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
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

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

def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result

#Test
#na = Node('a')
#nb = Node('b')
#nc = Node('c')
#e1 = WeightedEdge(na, nb, 15, 10)
##print e1
##print e1.getTotalDistance()
##print e1.getOutdoorDistance()
#e2 = WeightedEdge(na, nc, 14, 6)
#e3 = WeightedEdge(nb, nc, 3, 1)
##print e2
##print e3
#
#g = WeightedDigraph()
#g.addNode(na)
#g.addNode(nb)
#g.addNode(nc)
#g.addEdge(e1)
#g.addEdge(e2)
#g.addEdge(e3)
#print g

# Testcase Grader
#nh = Node('h')
#nj = Node('j')
#nk = Node('k')
#nm = Node('m')
#ng = Node('g')
#g = WeightedDigraph()
#g.addNode(nh)
#g.addNode(nj)
#g.addNode(nk)
#g.addNode(nm)
#g.addNode(ng)
#randomEdge = WeightedEdge(nm, nh, 90, 55)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nk, nj, 43, 34)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nk, nm, 11, 11)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nj, nk, 67, 47)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nj, nm, 86, 77)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nh, nm, 57, 19)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nh, nj, 81, 63)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nm, nk, 54, 46)
#g.addEdge(randomEdge)
#print g.childrenOf(nh)#: [m, j]
#print g.childrenOf(nj)#: [[k, (67.0, 47.0)], [m, (86.0, 77.0)]]
#print g.childrenOf(nk)#: [[j, (43.0, 34.0)], [m, (11.0, 11.0)]]
#print g.childrenOf(nm)#: [[h, (90.0, 55.0)], [k, (54.0, 46.0)]]
#print g.childrenOf(ng)#: []