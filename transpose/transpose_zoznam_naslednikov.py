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

def transpose(graph):
	newGraph = Graph_num1(graph.size + 1)

	for i in range(graph.size):
		for j in range(len(graph.succs[i])):
			weight = graph.succs[i][j][0]
			vertex = graph.succs[i][j][1]
			newGraph.succs[vertex].append((weight, i))
	return newGraph

print(transpose(graph1).succs)


