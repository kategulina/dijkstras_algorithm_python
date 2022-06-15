class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float("inf")
        self.previousVertex = None
        self.isVisited = False


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def computePath(self, sourceId):
        start_vertex = self.vertexes[sourceId]
        start_vertex.minDistance = 0
        count = 0
        while count != len(self.vertexes):
            minVertex = self.returnMinVertex()
            for edge in minVertex.edges:
                if not self.vertexes[edge.target].isVisited:
                    if edge.weight + minVertex.minDistance < self.vertexes[edge.target].minDistance: 
                        self.vertexes[edge.target].minDistance = edge.weight + minVertex.minDistance
                        self.vertexes[edge.target].previousVertex = minVertex
            minVertex.isVisited = True
            count += 1

    def returnMinVertex(self):
        minVertex = self.vertexes[0]
        index = 0
        while minVertex.isVisited:
            index += 1
            if index > len(self.vertexes):
                return None
            minVertex = self.vertexes[index]
        for vertex in self.vertexes:
            if not vertex.isVisited and vertex.minDistance < minVertex.minDistance:
                minVertex = vertex
        return minVertex

    def getShortestPathTo(self, targetId):
        path = []
        vertex = self.vertexes[targetId]
        while vertex is not None:
            path.append(vertex)
            vertex = vertex.previousVertex
        return path[::-1]

    def createGraph(self, vertexes, edgesToVertexes):
        for vertex in vertexes:
            for edge in edgesToVertexes:
                if vertex.id == edge.source:
                    vertex.edges.append(edge)
            self.vertexes.append(vertex)

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float("inf")
            vertex.isVisited = False
            vertex.previousVertex = None

    def getVertexes(self):
        return self.vertexes
