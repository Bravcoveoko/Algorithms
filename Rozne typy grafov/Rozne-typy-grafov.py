# Prikald 1)
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
#----------------------------------------------------
# Priklad 2)
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
#-------------------------------------------------
# Prikald 3)
# Neorientovany graf -> 1 je hrana, 0 neni hrana

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
#------------------------------------------------
# Priklad 4)
# Neorientovany graf
# Seznam nasledniku
class Graph_num4:
	def __init__(self, size):
		self.size = size
 		self.table = [[] for _ in range(size)]

graph4 = Graph_num4(10)
# vrchol 0 ukazuje do vrcholov 1, 6 a 8 ...
graph4.table = [[1, 6, 8],
  				[0, 4, 6, 9],
  				[4, 6],
  				[4, 5, 8],
  				[1, 2, 3, 5, 9],
  				[3, 4],
  				[0, 1, 2],
  				[8, 9],
  				[0, 3, 7],
  				[1, 4, 7]]
 #--------------------------------------------
 # Priklad 5)
 # Neorientovany graf cez maticu ohodnotene hrnay
 # Tam kde nebude hrana bude None 
 # MATICA JE SYMETRICKY ZOBRAZENA PODLA HL. DIAGONALY 
 # cize ak je hrana medzi vrcholom 4 a 5 tak je aj medzi 5 a 4 -> table[4][5] = 1 and table[5][4] = 1
 class Graph_num5:
 	def __init__(self, size):
 		self.size = size
 		self.table = [[None] for _ in range(size)]

graph5 = Graph_num5(10)
graph5.table = [[0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
				[1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
				[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
				[0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
				[0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
				[0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
				[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
				[1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
				[0, 1, 0, 0, 1, 0, 0, 1, 0, 0]]
#---------------------------------------------------
# Graf moze byt reprezentovany aj ako slovnik
class Graph_num6:
	def __init__(self, size):
		self.size = size
		self.dict = None
graph6 = Graph_num6(7)
graph6 = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}
#----------------------------------------------
# Neorientovany , ohodnoteny graf
class Graph_num7:
	def __init__(self, size):
		self.size = size
		self.dict = None
graph7 = Graph_num7(9)
graph7.dict = {
			0 : [(4, 1), (8, 7)],
			1 : [(4, 0), (8, 2), (11, 7)],
			2 : [(8, 1), (7, 3), (4, 5), (2, 8)],
			3 : [(7, 2), (14, 5), (9, 4)],
			4 : [(9, 3), (10, 5)],
			5 : [(4, 2), (14, 3), (10, 4), (2, 6)],
			6 : [(2, 5), (1, 7), (6, 8)],
			7 : [(8, 0), (11, 1), (1, 6), (7, 8)],
			8 : [(2, 2), (6, 6), (7, 7)]
}
# 0 : [(4, 1), (8, 7)] 
# vrchol 0 ukazuje do vrcholu 1 cez ohodnotenu hranu 4
# vrchol 0 ukazuje do vrcholu 7 cez ohodnoteny hranu 8
#-------------------------------------------------
