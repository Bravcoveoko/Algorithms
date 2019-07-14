class Graph_num1:
    def __init__(self, size):
        # pocet vrcholov
        self.size = size
        # seznam nasledniku
        self.succs = [[] for _ in range(size)]

graph1 = Graph_num1(7)
graph1.succs = [[(300, 4)], # vrchol 0 ukazuje do vrcholu 4 cez ohodnotenou hranou 300
                [(0, 3)],     # vrchol 1 ukaze do vrcholu 3 cez ohodnotenu hranu 0
                [(60, 5)],
                [(40, 4)],
                [(0, 6), (40, 0)],
                [(120, 6), (90, 7)], # vrchol 5 ukaze do vrcholu 6 a 7 cez ohodnotene hrany 120 a 90
                [(10, 5)],
                []]

class Vertex:
    def __init__(self):
        self.discovery = None
        self.finish = None
        self.color = "white"

def dfs_visit(graph, vertex, time, vertexArr, edges):
    time += 1
    vertexArr[vertex].discovery = time
    vertexArr[vertex].color = "grey"

    for i in range(len(graph.succs[vertex])):
        ver = graph.succs[vertex][i][1]
        if (vertexArr[ver].color == "white"):
            edges["treeEdge"] += 1
            dfs_visit(graph, ver, time, vertexArr, edges)
            time = vertexArr[ver].finish

        elif (vertexArr[ver].color == "grey"):
            edges["backEdge"] += 1
        elif (vertexArr[ver].color == "black"):
            ud = vertexArr[vertex].discovery
            vf = vertexArr[ver].finish
            print('U: ' + str(vertex) + ' d: ' + str(ud) + ' --- ' + 'V: ' + str(ver) + ' f: ' + str(vf))
            if (vf < ud and vertexArr[ver].color == "black"):
                edges["crossEdge"] += 1
            if (ud < vf and vertexArr[ver].color == "black"):
                edges["forwardEdge"] += 1

    time += 1
    vertexArr[vertex].finish = time
    vertexArr[vertex].color = "black"
    return

def allTypeEdges(graph):
    edges = {
        "treeEdge": 0,
        "backEdge": 0,
        "forwardEdge": 0,
        "crossEdge": 0
    }
    vertexArr = [Vertex() for _ in range(graph.size + 1)]
    time = 0

    for v in range(graph.size + 1):
        if (vertexArr[v].color == "white"):
            dfs_visit(graph, v, time, vertexArr, edges)
            time = vertexArr[v].finish
    index = 0
    for ver in vertexArr:
        print('Vrchol: ' + str(index) + ' dis: ' + str(ver.discovery) + ' fin: ' + str(ver.finish))
        index += 1
    return edges

ed = allTypeEdges(graph1)

for x, y in ed.items():
    print(x, y)



