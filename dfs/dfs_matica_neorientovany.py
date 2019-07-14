class Graph_num3:
	def __init__(self, size):
		# pocet vrcholov
		self.size = size
		self.table = [[] for _ in range(size)]

graph3 = Graph_num3(10)
				#0 #1  #2 #3 #4 #5 #6 #7 #8 #9
graph3.table = [[0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
				[1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
				[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
				[0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
				[0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
				[0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
				[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
				[1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
				[0, 1, 0, 0, 1, 0, 0, 1, 0, 0]]

# KLAISCKY DFS ---> NEFUNGUJE PRE NESUVISLE GRAFY 
def dfs_visit(graph, visited, path, vertex):
	visited[vertex] = True
	path.append(vertex)

	for ver in range(len(graph.table[vertex])):
		if (graph.table[vertex][ver] == 1):
			if (visited[ver] == False):
				dfs_visit(graph, visited, path, ver)

def dfs(graph):
	visited = [False] * graph.size
	path = []

	dfs_visit(graph, visited, path, 0)
	return path


print(dfs(graph3))