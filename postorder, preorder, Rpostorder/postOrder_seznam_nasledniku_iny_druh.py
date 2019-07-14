class Graph_num2:
	def __init__(self, size):
		self.size = size
		self.succs = [[] for _ in range(size)]

graph2 = Graph_num2(11)
graph2.succs = [[1, 3], [2], [0], [4], [5], [3], [7], [8], [9], [6, 10], []]

# NEFUNGUJE PRE NESUVISLE GRAFY
# V Path je POSOTDER -> rozdiel je iba v tom path.append(vertex) sa da nakoniec cyklu 
def dfs_visit(graph, visited, path, vertex):
	visited[vertex] = True
	print(vertex)

	for i in range(len(graph.succs[vertex])):
		ver = graph.succs[vertex][i]
		if (visited[ver] == False):
			dfs_visit(graph, visited, path, ver)
	path.append(vertex)

def dfs(graph):
	visited = [False] * graph.size
	path = []

	for i in range(len(visited)):
		if (visited[i] == False):
			#print(visited)
			dfs_visit(graph, visited, path, i)
	return path


print(dfs(graph2))