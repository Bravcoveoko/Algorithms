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
graph2.succs = [[2], [1, 0, 4, 2], [1], [1], []]

# KLAISCKY DFS ---> NEFUNGUJE PRE NESUVISLE GRAFY 
def dfs_visit(graph, visited, path, vertex):
	visited[vertex] = True
	path.append(vertex)

	for i in range(len(graph.succs[vertex])):
		ver = graph.succs[vertex][i]
		if (visited[ver] == False):
			dfs_visit(graph, visited, path, ver)

def dfs(graph):
	visited = [False] * graph.size
	path = []

	dfs_visit(graph, visited, path, 0)
	return path


print(dfs(graph2))