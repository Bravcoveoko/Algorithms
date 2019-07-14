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

# DFS nepotrebuje zadny zasobnik
# Zasobnik 'vznika' postupnym zanorovanim sa rekurzie
# NEFUNGUJE NA NESUVISLE GRAFY !!!!
# v Path je postorder !!
# rozdiel je iba v tom path.append(vertex) sa da nakoniec cyklu
def dfs_visit(graph, visited, path, vertex):
	visited[vertex] = True

	for i in range(len(graph.succs[vertex])):
		ver = graph.succs[vertex][i][1]
		if (visited[ver] == False):
			dfs_visit(graph, visited, path, ver)
	path.append(vertex)


def dfs(graph):
	visited = [False] * (graph.size + 1)
	path = []

	dfs_visit(graph, visited, path, 0)

	return path


print(dfs(graph1))