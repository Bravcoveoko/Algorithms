from collections import deque
class Graph_num1:
	def __init__(self, size):
		# pocet vrcholov
		self.size = size
		# seznam nasledniku
		self.succs = [[] for _ in range(size)]

graph1 = Graph_num1(9)
graph1.succs = [[(300, 4)], # vrchol 0 ukazuje do vrcholu 4 cez ohodnotenou hranou 300
				[(0, 3)], 	# vrchol 1 ukaze do vrcholu 3 cez ohodnotenu hranu 0
				[(60, 5)],
				[(40, 4)],
				[(0, 6)],
				[(120, 6), (90, 7)], # vrchol 5 ukaze do vrcholu 6 a 7 cez ohodnotene hrany 120 a 90
				[],
				[],
				[(100, 9)], 
				[(50, 8)]]

# Toto je nesuvisly graf -> vrcholu 8 a 9 su mimo 

def mainBFS(graph, vertex, visited, path):
	queue = deque()
	visited[vertex] = True
	queue.append(vertex)

	while queue:
		currentVertex = queue.popleft()
		path.append(currentVertex)

		for i in range(len(graph.succs[currentVertex])):
			ver = graph.succs[currentVertex][i][1]
			if (visited[ver] == False):
				queue.append(ver)
				visited[ver] = True


# Rozdiel oproti klasickemu BFs je ten ze obsahuje funkciu respektive
# obsahuje cyklus ktory prechadza cez uplne vsetky vrcholu nie len ako ide klasicke BFS
# 
def startingBFS(graph):
	visited = [False] * (graph.size + 1)
	path = []
	# Keby si chcel upravit program tak ze startingBFS bude brat dva argumenty
	# kde ten druhy argument bude zaciatocny vrchol, tak sem
	# TODO
	# pusti klasicky bfs ktory sa nachadza v zlozke bfs
	# trosku ho treba upravit aby bral dalsie argumenty pre naplneni path a zmenu visited.
	# prvym pustenim zistis ktore neboli odhalene a tie poodhalujes potom vo for cykle
	for vertex in range(len(visited)):
		if (visited[vertex] == False):
			mainBFS(graph, vertex, visited, path)
	return path

print(startingBFS(graph1))

# Trosku vylepseny BFS
# Pouzita classa Vertex -> vsetko sa predava ako object a pracujes s nimi
# path mozes zrusit -> vsetko sa to vypisuje rekurzive 
# keby chces path naplnit tak vo funkcii parents nebudes vypisovat ale naplnat pole 
"""class Vertex:
	def __init__(self):
		self.name = None
		self.distance = 0
		self.color = "w"
		self.parent = None

def mainBfs(graph, allVertex, ver):
	allVertex[ver].color = "g"
	queue = deque()
	queue.append(ver)

	while queue:
		currentVer = queue.popleft()
		for w, v in graph.succs[currentVer]:
			if (allVertex[v].color == "w"):
				allVertex[v].color = "g"
				allVertex[v].distance = allVertex[currentVer].distance + 1
				allVertex[v].parent = allVertex[currentVer]
				queue.append(v)
		allVertex[currentVer].color = "b"

# Len pridaj druhy argument ...neake prazdne pole a ponaplnaj ho
# alebo staci ak pri zarazke urobis toto: return [ver]
# to by malo stacit	
def parents(ver):
	if (ver.parent == None):
		print("-> ", ver.name, end="")
		return
	parents(ver.parent)
	print(" -> ", end="")
	print(ver.name, end="")

def bfs(graph):
	allVertex = []
	for i in range(graph.size + 1):
		allVertex.append(Vertex())
		allVertex[i].name = i

	for ver in range(graph.size + 1):
		if allVertex[ver].color == "w":
			mainBfs(graph, allVertex, ver)
	# Vypis vrcholov (vsetko okrem color) + ako sa do nich dostat
	for ver in allVertex:
		print("Vertex: ", ver.name, end="")
		print(" Distance: ", ver.distance, end="")
		if (ver.parent == None):
			print(" Parent: ", ver.parent, end="")
		else:
			print(" Parent: ", ver.parent.name, end="")
		print(" Path: ", end="")
		parents(ver)
		print()

bfs(graph1)"""



