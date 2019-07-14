from collections import deque
class Graph_num2:
	def __init__(self, size):
		self.size = size
		self.succs = [[] for _ in range(size)]

graph2 = Graph_num2(11)
graph2.succs = [[1, 3], [2], [0], [4], [5], [3], [7], [8], [9], [6, 10], []]

graph3 = Graph_num2(8)
graph3.succs = [[1], [2, 4, 5], [3, 6], [2, 7], [0, 5], [6], [5], [3, 6]]

graph4 = Graph_num2(12)
graph4.succs = [[1], [2, 3, 4], [5], [], [1, 5, 6], [2, 7], [7, 9], [10], [6], [8], [11], [9]]

def dfs_visit(graph, visited, path, vertex):
	visited[vertex] = True
	path.append(vertex)

	for i in range(len(graph.succs[vertex])):
		ver = graph.succs[vertex][i]
		if (visited[ver] == False):
			dfs_visit(graph, visited, path, ver)

def dfs(graph):
	visited = [False] * graph.size
	path = deque()

	for i in range(len(visited)):
		if (visited[i] == False):
			dfs_visit(graph, visited, path, i)
	return path

def transpose(graph):
	newGraph = Graph_num2(graph.size)

	for i in range(graph.size):
		for j in range(len(graph.succs[i])):
			vertex = graph.succs[i][j]
			newGraph.succs[vertex].append(i)
	return newGraph

def stronglyConnectedComponents(graph):
	# Naplni sa queue povodny grtafov
	queue = dfs(graph)
	result = []

	transpseGrahp = transpose(graph)

	visited = [False] * graph.size
	while queue:
		# predtym tam bolo pole a pouzival sa pop(0) -> a to ma zlozitost O(n)
		# Zmenil som to na queue kde popleft ma zlozitost O(1)
		# Mozne riesenie cez pole -> urobit reverse toho pola a brat posledny pop(-1) to je potom zlozitost O(1)
		v = queue.popleft()
		arr = []
		if (visited[v] == False):
			dfs_visit(transpseGrahp, visited, arr, v)
			result.append(arr)
	return result

print(stronglyConnectedComponents(graph2))
print(stronglyConnectedComponents(graph3))
print(stronglyConnectedComponents(graph4))













