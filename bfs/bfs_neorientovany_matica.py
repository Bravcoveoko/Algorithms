from collections import deque
class Graph_num3:
	def __init__(self, size):
		# pocet vrcholov
		self.size = size
		self.table = [[] for _ in range(size)]

graph3 = Graph_num3(10)
				#0 #1  #2 #3 #4 #5 #6 #7 #8 #9 #10
graph3.table = [[0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
				[1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
				[0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
				[0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
				[0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
				[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
				[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
				[1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
				[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]]

def bfs(graph, start_vertex):
	path = []
	visited = [False] * graph.size
	queue = deque()
	queue.append(start_vertex)
	visited[start_vertex] = True

	while queue:
		currentVertex = queue.popleft()
		path.append(currentVertex)

		for i in range(len(graph.table[currentVertex])):
			if (graph.table[currentVertex][i] == 1):
				if (visited[i] == False):
					queue.append(i)
					visited[i] = True
	print(path)

bfs(graph3, 0)








