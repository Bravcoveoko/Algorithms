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

	for ver in range(len(graph.table[vertex])):
		if (graph.table[vertex][ver] == 1):
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

dfs(graph3)