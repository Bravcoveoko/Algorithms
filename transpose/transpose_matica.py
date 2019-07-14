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

def transpose(graph):
	newGraph = Graph_num3(graph.size)

	for i in range(graph.size):
		for j in range(graph.size):
			if graph.table[i][j] == 0:
				newGraph.table[i].append(1)
			else:
				newGraph.table[i].append(0)
	return newGraph

# Netusim ci neorientovany graf moze byt transponovany 
# Ale toto "funguje"