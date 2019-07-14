class Graph_num1:
	def __init__(self, size):
		# pocet vrcholov
		self.size = size
		# seznam nasledniku
		self.succs = [[] for _ in range(size)]

# Tu cyklus neni
graph1 = Graph_num1(7)
graph1.succs = [[(300, 4)], # vrchol 0 ukazuje do vrcholu 4 cez ohodnotenou hranou 300
				[(0, 3)], 	# vrchol 1 ukaze do vrcholu 3 cez ohodnotenu hranu 0
				[(60, 5)],
				[(40, 4)],
				[(0, 6)],
				[(120, 6), (90, 7)], # vrchol 5 ukaze do vrcholu 6 a 7 cez ohodnotene hrany 120 a 90
				[],
				[]]

# Tu je cyklus
graph2 = Graph_num1(7)
graph2.succs = [[(300, 4)], # vrchol 0 ukazuje do vrcholu 4 cez ohodnotenou hranou 300
				[(0, 3)], 	# vrchol 1 ukaze do vrcholu 3 cez ohodnotenu hranu 0
				[(60, 5)],
				[(40, 4)],
				[(0, 6), (20, 5)],
				[(120, 6), (90, 7)],
				[],
				[(50, 0)]]

# Dalsi co ma cyklus
graph3 = Graph_num1(6)
graph3.succs = [[(100, 4)],
				[],
				[(50, 5)],
				[(50, 4)],
				[(80, 1), (40, 5)],
				[(30, 6)],
				[(50, 0)]]

def isCyclicRec(graph, vertex, visited, stack):
	visited[vertex] = True
	stack[vertex] = True

	for i in range(len(graph.succs[vertex])):
		ver = graph.succs[vertex][i][1]
		if (visited[ver] == False):
			if isCyclicRec(graph, ver, visited, stack):
				return True
		elif (stack[ver] == True):
			return True
	stack[vertex] = False
	return False

def isCyclic(graph):
	visited = [False] * (graph.size + 1)
	stack = [False] * (graph.size + 1)

	for ver in range(len(visited)):
		if (visited[ver] == False):
			if (isCyclicRec(graph, ver, visited, stack)):
				return True
	return False

print(isCyclic(graph1))
print(isCyclic(graph2))
print(isCyclic(graph3))

# ----- TOTO JE SPRAVENE CEZ FARBY-----
# Hento je kokotina ...Este to je aj pamatovo horise kvoli stack polu
# Ale bacha -> toto kontroluje ci je Acyklicky
# Bud to na zneguj nakonci alebo pomen True za False a naopak
"""def isAcylicRec(graph, colors, vertex):
	print()
	colors[vertex] = "g"
	print("Current: ", vertex, end=": ")
	for w, v in graph.succs[vertex]:
		print(v, end=" ")
		if (colors[v] == "w"):
			if isAcylicRec(graph, colors, v):
				continue
		if (colors[v] == "g"):
			return False
	colors[vertex] = "b"
	return True


def isAcylic(graph):
	colors = ["w"] * (graph.size + 1)

	for ver in range(graph.size + 1):
		if colors[ver] == "w":
			if not isAcylicRec(graph, colors, ver):
				return False
	return True"""