from queue import PriorityQueue

class Vertex:
  def __init__(self, name):
    self.name = name
    self.edges = []
    self.visited = False

  def connect(self, ad_vertex, edge_cost):
    global totalEdges
    self.edges.append(Edge(self, ad_vertex, edge_cost))
    ad_vertex.edges.append(Edge(ad_vertex, self, edge_cost))
    totalEdges += 2
    
  def __repr__(self):
    return self.name


class Edge:
  def __init__(self, _from, _to, _cost):
    self._from = _from
    self._to = _to
    self._cost = _cost

  def __lt__(self, other):
    if isinstance(other, Edge):
      return self._cost < other._cost
    return False

  #string representation of the edge class
  def __repr__(self):
    return f"{self._from}-----{self._to}"


class Prims:
  def __init__(self):
    self.pqueue = PriorityQueue()
    self.mst = []
    self.totalCost = 0

  #function implementing Prim's algorithm
  def findMST(self, s):
    global totalEdges

    #add all edges of the starting vertex
    self.addEdges(s)
    edgeCount = 0

    while not self.pqueue.empty() and edgeCount != totalEdges:
      #pop the low cost edge from PriorityQueue
      minEdge = self.pqueue.get()

      
      if minEdge._to.visited:
        continue
      else:
        #increment count and add edge to MST
        edgeCount += 1
        self.totalCost += minEdge._cost
        self.mst.append(minEdge)
        self.addEdges(minEdge._to)

    return edgeCount != totalEdges

  def addEdges(self, s):
    s.visited = True;
    for edge in s.edges:
      if not edge._to.visited:
        self.pqueue.put(edge)


if __name__ == '__main__':
  totalEdges = 0

  vertices = [Vertex('0'), Vertex('1'), Vertex('2'), Vertex('3'), Vertex('4'),Vertex('5'),Vertex('6')]

  #connecting vertices
  vertices[0].connect(vertices[3], 1)
  vertices[0].connect(vertices[1], 2)
  vertices[0].connect(vertices[4], 4)
  vertices[2].connect(vertices[3], 2)
  vertices[2].connect(vertices[5], 4)
  vertices[5].connect(vertices[4], 3)
  vertices[5].connect(vertices[6], 2)
  vertices[6].connect(vertices[4], 6)
  
  #driver code
  prims = Prims()
  if prims.findMST(vertices[0]):
    print(prims.mst)
    print("Total Cost: ",prims.totalCost)
  else:
    print("MST is not possible for given graph")