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

# Timetag classa -> bude v poli (index pola == vrchol)
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
		ver = graph.succs[vertex][i][1]
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

dfs(graph1)