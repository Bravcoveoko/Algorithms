from collections import deque
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
			if (visited[ver] == False):
				queue.append(ver)
				visited[ver] = True
	print(path)

bfs(graph2, 0)