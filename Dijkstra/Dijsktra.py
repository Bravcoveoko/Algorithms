import math
class Graph_num7:
    def __init__(self, size):
        self.size = size
        self.table = None
g  = Graph_num7(9) 
g.table = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# Algoritmus ma zlozitost O(V^2) !!

def minDistance(graph, distance, shortestTree):
    m = math.inf
    for v in range(graph.size):
        if distance[v] < m and shortestTree[v] == False:
            m = distance[v]
            minindex = v
    return minindex

def Dijkstra(graph, src_vertex):
    distance = [math.inf] * graph.size
    distance[src_vertex] = 0
    shortestTree = [False] * graph.size

    for i in range(graph.size):
        u = minDistance(graph, distance, shortestTree)

        shortestTree[u] = True

        for ver in range(graph.size):
            weight = graph.table[u][ver]
            if weight > 0 and shortestTree[ver] == False and distance[ver] > distance[u] + weight:
                distance[ver] = distance[u] + weight
    print("Vertex tDistance from Source")
    for n in range(graph.size):
        print(n, distance[n])

Dijkstra(g, 0)

