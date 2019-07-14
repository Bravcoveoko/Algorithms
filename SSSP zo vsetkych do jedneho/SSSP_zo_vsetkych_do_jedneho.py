import math
from collections import deque
# Priklad 2)
class Graph_num2:
	def __init__(self, size):
		self.size = size
		self.succs = [[] for _ in range(size)]

graph2 = Graph_num2(7)
# vrchol 0 ukazuje do vrcholu 2
# vrchol 1 ukazuje do vrcholov 1, 0, 4 a 2
# vrchol 2 ukazuje do vecholu 1
# vrchol 3 ukazuje do vrcholu 1
# vrchol 4 neukazuje nikde
				#0       #1        #2   #3   #4
graph2.succs = [[1, 2], [0], [], [0], [3], [0], [1]]

def transpose(graph):
	newGraph = Graph_num2(graph.size)

	for i in range(graph.size):
		for j in range(len(graph.succs[i])):
			vertex = graph.succs[i][j]
			newGraph.succs[vertex].append(i)
	return newGraph

def __bfs(graph, vertex, timeMark):
	queue = deque()
	queue.append(vertex)
	timeMark[vertex] = 0

	while queue:
		current_vertex = queue.popleft()

		for ver in graph.succs[current_vertex]:
			if (timeMark[ver] == math.inf):
				queue.append(ver)
				timeMark[ver] = timeMark[current_vertex] + 1



def fromAllToOne(graph, toVertex):
	timeMark = [math.inf] * graph.size
	newG = transpose(graph)
	__bfs(newG, toVertex, timeMark)
	for i in range(graph.size):
		print("Vrchol: ", i, " Vzdialenost: ", timeMark[i])

fromAllToOne(graph2, 0)


