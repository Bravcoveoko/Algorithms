class Graph_num2:
	def __init__(self, size):
		self.size = size
		self.succs = [[] for _ in range(size)]

graph2 = Graph_num2(5)
# vrchol 0 ukazuje do vrcholu 2
# vrchol 1 ukazuje do vrcholov 1, 0, 4 a 2
# vrchol 2 ukazuje do vecholu 1
# vrchol 3 ukazuje do vrcholu 1
# vrchol 4 neukazuje nikde
				#0       #1        #2   #3   #4
graph2.succs = [[2], [0, 4, 2], [], [1], []]

graph3 = Graph_num2(6)
graph3.succs = [[1, 2, 3, 4, 5], [], [1], [1], [], []]

def isCyclicRec(graph, vertex, visited, stack):
	visited[vertex] = True
	stack[vertex] = True

	for i in range(len(graph.succs[vertex])):
		ver = graph.succs[vertex][i]
		if (visited[ver] == False):
			if isCyclicRec(graph, ver, visited, stack):
				return True
		elif (stack[ver] == True):
			return True
	stack[vertex] = False
	return False

def isCyclic(graph):
	visited = [False] * (graph.size)
	stack = [False] * (graph.size)

	for ver in range(len(visited)):
		if (visited[ver] == False):
			if (isCyclicRec(graph, ver, visited, stack)):
				return True
	return False

print(isCyclic(graph3))# ----- TOTO JE SPRAVENE CEZ FARBY-----
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
