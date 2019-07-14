import math
class Graph_num1:
    def __init__(self, size):
        # pocet vrcholov
        self.size = size
        # seznam nasledniku
        self.succs = [[] for _ in range(size)]

# Toto je acyklicky, ohonoteny a orientovany graf
graph1 = Graph_num1(4)
graph1.succs = [[(-1, 1), (4, 2)], # vrchol 0 ukazuje do vrcholu 4 cez ohodnotenou hranou 300
                [(3, 2), (-4, 3), (2, 4)],   # vrchol 1 ukaze do vrcholu 3 cez ohodnotenu hranu 0
                [],
                [(5, 2)],
                [(-3, 3)]]

"""Rozdiel oproti klasickemu Bellman-Ford algo. je ten ze graf co dostaneme
musi byt acyklicky, lebo potom mozme aplikovat topologicke usporiadanie a na tomto 
usporiadani mozme pustit bellmana ... zlozitost je O(V + E)"""
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


def topologicalSort(graph):
    visited = [False] * (graph.size + 1)
    path = []

    for v in range(len(visited)):
        if (visited[v] == False):
            topologicalSortRec(graph, visited, path, v)

    return path[::-1]

def DAG(graph, start_vertex):
    allVertex = [Vertex() for _ in range(graph.size + 1)]
    topoArr = topologicalSort(graph)
    Init_SSSP(start_vertex, allVertex)

    for u in topoArr:
        for w, v in graph.succs[u]:
            if allVertex[v].distance > allVertex[u].distance + w and allVertex[u] != math.inf:
                    Relax(allVertex[u], allVertex[v], w)
    # Vypis
    print("Vertex   Distance from Source") 
    for i in range(graph.size + 1):
        print("%d \t\t %d" % (i, allVertex[i].distance))

DAG(graph1, 0)