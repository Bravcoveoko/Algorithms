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


class TimeTag:
	def __init__(self):
		self.discovery = None
		self.finish = None
# DFS 
# timetagArr je pole
def dfs_visit(graph, visited, path, vertex, time, timetagArr):
	visited[vertex] = True
	time += 1
	timetagArr[vertex].discovery = time
	path.append(vertex)

	for i in range(len(graph.succs[vertex])):
		ver = graph.succs[vertex][i]
		if (visited[ver] == False):
			dfs_visit(graph, visited, path, ver, time, timetagArr)
			time = timetagArr[ver].finish
	time += 1
	timetagArr[vertex].finish = time
	return


# funguje iba na SUVISLE GRAFY !!!!!!!
def dfs(graph):
	visited = [False] * (graph.size + 1)
	timetagArr = [TimeTag() for _ in range(graph.size + 1)]
	path = []
	time = 0

	dfs_visit(graph, visited, path, 0, time, timetagArr)

	print(path)
	for i in range(graph.size + 1):
		print('d: ' + str(timetagArr[i].discovery) + ' f: ' + str(timetagArr[i].finish), end=" | ")

dfs(graph2)