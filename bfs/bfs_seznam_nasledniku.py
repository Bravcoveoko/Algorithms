from collections import deque
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


def bfs(graph, start_vertex):
	path = []
	visited = [False] * graph.size
	queue = deque()
	queue.append(start_vertex)
	visited[start_vertex] = True

	while queue:
		currentVertex = queue.popleft()
		path.append(currentVertex)

		for ver in graph.succs[currentVertex]:
			if (visited[ver[1]] == False):
				queue.append(ver[1])
				visited[ver[1]] = True
	print(path)

bfs(graph1, 0)







