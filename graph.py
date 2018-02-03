class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]





g = Graph()
for i in range(27):
    g.addVertex(i)
g.getVertices
g.addEdge(0,1,.5)
g.addEdge(0,3,.5)
g.addEdge(1,2,.5)
g.addEdge(1,4,.5)
g.addEdge(1,0,.5)
g.addEdge(2,1,.5)
g.addEdge(3,4,.5)
g.addEdge(2,5,.5)
g.addEdge(3,0,.5)
g.addEdge(3,6,.5)
g.addEdge(4,3,.5)
g.addEdge(4,1,.5)
g.addEdge(4,5,.5)
g.addEdge(4,7,.5)
g.addEdge(5,2,.5)
g.addEdge(5,4,.5)
g.addEdge(5,8,.5)
g.addEdge(6,3,.5)
g.addEdge(6,9,.5)
g.addEdge(6,7,.5)
g.addEdge(7,4,.5)
g.addEdge(7,6,.5)
g.addEdge(7,8,.5)
g.addEdge(7,10,.5)
g.addEdge(8,5,.5)
g.addEdge(8,7,.5)
g.addEdge(8,11,.5)
g.addEdge(9,6,.5)
g.addEdge(9,10,.5)
g.addEdge(9,12,.5)
g.addEdge(10,7,.5)
g.addEdge(10,9,.5)
g.addEdge(10,11,.5)
g.addEdge(10,13,.5)
g.addEdge(11,8,.5)
g.addEdge(11,14,.5)
g.addEdge(11,10,.5)
g.addEdge(12,9,.5)
g.addEdge(12,13,.5)
g.addEdge(12,15,.5)
g.addEdge(13,10,.5)
g.addEdge(13,16,.5)
g.addEdge(13,12,.5)
g.addEdge(13,14,.5)
g.addEdge(14,11,.5)
g.addEdge(14,13,.5)
g.addEdge(14,17,.5)
g.addEdge(15,12,.5)
g.addEdge(15,16,.5)
g.addEdge(15,18,.5)
g.addEdge(16,13,.5)
g.addEdge(16,15,.5)
g.addEdge(16,19,.5)
g.addEdge(16,17,.5)
g.addEdge(17,20,.5)
g.addEdge(17,14,.5)
g.addEdge(17,16,.5)
g.addEdge(18,15,.5)
g.addEdge(18,19,.5)
g.addEdge(18,21,.5)
g.addEdge(19,22,.5)
g.addEdge(19,16,.5)
g.addEdge(19,18,.5)
g.addEdge(19,20,.5)
g.addEdge(20,19,.5)
g.addEdge(20,17,.5)
g.addEdge(20,23,.5)
g.addEdge(21,18,.5)
g.addEdge(21,22,.5)
g.addEdge(21,24,.5)
g.addEdge(22,25,.5)
g.addEdge(22,19,.5)
g.addEdge(22,21,.5)
g.addEdge(22,23,.5)
g.addEdge(23,20,.5)
g.addEdge(23,22,.5)
g.addEdge(23,26,.5)
g.addEdge(24,25,.5)
g.addEdge(24,21,.5)
g.addEdge(25,24,.5)
g.addEdge(25,26,.5)
g.addEdge(25,22,.5)
g.addEdge(26,25,.5)
g.addEdge(26,23,.5)

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
