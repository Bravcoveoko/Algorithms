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

def transpose(graph):
	newGraph = Graph_num2(graph.size)

	for i in range(graph.size):
		for j in range(len(graph.succs[i])):
			vertex = graph.succs[i][j]
			newGraph.succs[vertex].append(i)
	return newGraph


print(transpose(graph2).succs)
