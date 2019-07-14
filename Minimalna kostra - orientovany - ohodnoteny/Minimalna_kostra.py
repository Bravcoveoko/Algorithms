class Graph_num7:
    def __init__(self, size):
        self.size = size
        self.succs = None
graph7 = Graph_num7(9)
graph7.succs = [ 
            (0, 4, 1), (0, 8, 7),
            (1, 8, 2), (1, 11, 7),
            (2, 7, 3), (2, 4, 5), (2, 2, 8),
            (3, 14, 5), (3, 9, 4),
            (4, 10, 5),
            (5, 2, 6),
            (6, 1, 7), (6, 6, 8),
            (7, 7, 8),
]

# !!! ak bude matica .. bude fajn si extrahovat iba hrany ktore maju True alebo 1 alebo 
# inac ako su repzrentovane
# tento algo funguje iba na NEORIENTOVANE OHODNOTENE GRAFY

# Musime zoradit hrany podla hodnoty od najmensieho po najvacsi
def sorted(graph):
    lenght = graph.size
    graph.succs.sort(key = lambda x: x[1])

def find(parent, ver):
    if (parent[ver] == ver):
        return ver
    return find(parent, parent[ver])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def Kruskal_spanning_tree(graph):
    # Hrany su zoradene od najmensieho po najvacsi
    sorted(graph)
    result = []

    # Algoritmus funguje s datovou strukturou Disjoin set
    # Vytvaraju sa mnoziny ktore sa potom zjednotia ak sa najdu neake vecholy ktore su v dvoch
    # rozdielnych mnozinach, inac sa ignoruje a while cyklus ide dalej
    parent = []
    rank = []
    i = 0
    e = 0
    # Inicializuj vsetkym Vertexom ich id
    for ver in range(graph.size):
        parent.append(ver)
        rank.append(0)
    while e < graph.size - 1:
        u, w, v = graph.succs[i]
        print(graph.succs[i])
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)
    # Toto sluzi na vypis 
    for u,v,weight  in result: 
        print ("%d -- %d == %d" % (u,v,weight))


Kruskal_spanning_tree(graph7)
