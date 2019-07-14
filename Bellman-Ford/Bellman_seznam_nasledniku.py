import math
class Graph_num1:
	def __init__(self, size):
		# pocet vrcholov
		self.size = size
		# seznam nasledniku
		self.succs = [[] for _ in range(size)]

graph1 = Graph_num1(4)
graph1.succs = [[(-1, 1), (4, 2)], # vrchol 0 ukazuje do vrcholu 1 cez ohodnotenou hranou -1 ...
				[(3, 2), (2, 3), (2, 4)], 	# vrchol 1 ukaze do vrcholu 2 cez ohodnotenu hranu 3
				[],
				[(5, 2), (1, 1)],
				[(-3, 3)]]

class Vertex:
	def __init__(self):
		# Name je len nazov toho vrcholu: cize 0, 1, 2 ... graph.size
		# sluzi na vypisovanie v rekurzii
		self.name = None
		self.distance = math.inf
		self.parent = None

def Relax(u, v, w):
	v.distance = u.distance + w
	# Priraduje sa object Vertex nie cislo !
	v.parent = u

def Init_SSSP(start_vertex, allVertex):
	allVertex[start_vertex].parent = start_vertex
	allVertex[start_vertex].distance = 0

# Rekurzia, kt. sluzi iba na vypisovanie cesty 
def recPath(start_vertex, ver, allVertex):
	if ver.name == 'A':
		print(ver.name, end="")
		return
	recPath(start_vertex, ver.parent, allVertex)
	print(" -> ", end="")
	print(ver.name, end="")
	

# start_vertex je cislo ....ale vypisujem pismena bacha na to
def Bellman_Ford(graph, start_vertex):
	allVertex = [Vertex() for _ in range(graph.size + 1)]
	for i in range(graph.size + 1):
		# funkcia chr meni ordinalnu hodnotu na pisemno 
		# 65 -> A
		# 66 -> B ...
		allVertex[i].name = chr(65 + i)
	# Inicializacia
	Init_SSSP(start_vertex, allVertex)
	# for i = 1 to |V|-1 do 
	for i in range(graph.size):
		for u in range(graph.size + 1):
			for w, v in graph.succs[u]:
				if allVertex[v].distance > allVertex[u].distance + w and allVertex[u] != math.inf:
					Relax(allVertex[u], allVertex[v], w)
	# Kontrola ci je cyklus zapornej dlzky
	for u in range(graph.size + 1):
		for w, v in graph.succs[u]:
			if allVertex[v].distance > allVertex[u].distance + w and allVertex[u] != math.inf:
				return None
	# Hlavny algortimus konci, to co je pod tymto komentom su len veci na vypis
	# Vypisovanie
	# Vrchol -> aka dlaha je najkrasia cesta 
	print("Vertex   Distance from Source") 
	for i in range(graph.size + 1):
		print("%d \t\t %d" % (i, allVertex[i].distance))
	print("--------- CESTY ---------")

	# Vypis cesty. Cez ake vrcholy sme museli prejst
	for i in range(graph.size + 1):
		print("Vertex: " + str(i) + "| ", end="")
		recPath(start_vertex, allVertex[i], allVertex)
		print()

Bellman_Ford(graph1, 0)