class Graph_num1:
	def __init__(self, size):
		# pocet vrcholov
		self.size = size
		# seznam nasledniku
		self.succs = [[] for _ in range(size)]

graph1 = Graph_num1(7)
graph1.succs = [[(300, 4)], # vrchol 0 ukazuje do vrcholu 4 cez ohodnotenou hranou 300
				[(0, 3)], 	# vrchol 1 ukaze do vrcholu 3 cez ohodnotenu hranu 0
				[(60, 5)],
				[(40, 4)],
				[(0, 6)],
				[(120, 6), (90, 7)], # vrchol 5 ukaze do vrcholu 6 a 7 cez ohodnotene hrany 120 a 90
				[],
				[]]

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


print(topologicalSort(graph1))