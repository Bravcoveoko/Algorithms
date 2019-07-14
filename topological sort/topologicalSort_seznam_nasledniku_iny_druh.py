class Graph_num2:
	def __init__(self, size):
		self.size = size
		self.succs = [[] for _ in range(size)]

graph2 = Graph_num2(4)
graph2.succs = [[], [0], [], [1, 2]]

# Topologicke usporiadanie 
# Funguje iba na acyklickych orientovanych grafoch
# Myslienka: Pustit dfs ale tak aby v path bolo postorder potom nakonci len vrat obratene path
# vid return path[::-1]
# V rieseniach na nete pouzivaju insert funkciu ..avsak ta ma O(n) ..cize celkova zlozitost by bola neaka moc vvysoka ba ci aj kvadraticka
# TENTO FUNGUJE AJ NA NESUVISLE GRAFY

# Tato funkcia je vlastne dfs len inac pomenovana :) 
def topologicalSortRec(graph, visited, path, vertex):
	visited[vertex] = True

	for i in range(len(graph.succs[vertex])):
		ver = graph.succs[vertex][i]
		if (visited[ver] == False):
			topologicalSortRec(graph, visited, path, ver)
	path.append(vertex)


def topologicalSort(graph):
	visited = [False] * (graph.size)
	path = []

	for v in range(len(visited)):
		if (visited[v] == False):
			topologicalSortRec(graph, visited, path, v)

	return path[::-1]


print(topologicalSort(graph2))