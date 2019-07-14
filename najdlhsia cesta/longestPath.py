# Prikald 1)
import math
class Graph_num1:
    def __init__(self, size):
        # pocet vrcholov
        self.size = size
        # seznam nasledniku
        self.succs = [[] for _ in range(size)]

graph1 = Graph_num1(6)
graph1.succs = [[(5, 1), (3, 2)],
                [(2, 2), (6, 3)],
                [(7, 3), (4, 4), (2, 5)],
                [(-1, 4), (1, 5)],
                [(-2, 5)],
                []]

##### GRAF MUSI BYT ACYKLICKY ######
### ZLOZITOST: O(V + E) #######
class Vertex:
    def __init__(self):
        self.distance = math.inf
        self.parent = None

def Relax(u, v, w):
    v.distance = u.distance + w
    v.parent = u

def Init_SSSP(start_vertex, allVertex):
    allVertex[start_vertex].parent = start_vertex
    allVertex[start_vertex].distance = 0

def topologicalSortRec(graph, visited, path, vertex):
    visited[vertex] = True

    for i in range(len(graph.succs[vertex])):
        ver = graph.succs[vertex][i][1]
        if (visited[ver] == False):
            topologicalSortRec(graph, visited, path, ver)
    path.append(vertex)

# Topologicke usporiadanie -> Iba ak je graf acyklicky
def topologicalSort(graph):
    visited = [False] * (graph.size)
    path = []

    for v in range(len(visited)):
        if (visited[v] == False):
            topologicalSortRec(graph, visited, path, v)

    return path[::-1]

# Do dvojic sa neda priradit (mozno moja nevedomost) tak si vytvorim
# novy graf kde len hodnost hrany vynasobim -1
def makeEdgesNegative(graph):
    newG = Graph_num1(graph.size)

    for i in range(graph.size):
        for j in range(len(graph.succs[i])):
            weight = graph.succs[i][j][0]
            vertex = graph.succs[i][j][1]
            newG.succs[i].append((weight * - 1, vertex))
    return newG


def longestPath(graph, start_vertex):
    newGraph = makeEdgesNegative(graph)
    topoSort = topologicalSort(graph)
    allVertex = [Vertex() for _ in range(graph.size)]
    Init_SSSP(start_vertex, allVertex)
    print(topoSort)

    for u in topoSort:
        for w, v in newGraph.succs[u]:
            if allVertex[v].distance > allVertex[u].distance + w:
                Relax(allVertex[u], allVertex[v], w)
    print("Vertex   Distance from Source") 
    for i in range(graph.size):
        print((i, allVertex[i].distance * -1))


longestPath(graph1, 1)