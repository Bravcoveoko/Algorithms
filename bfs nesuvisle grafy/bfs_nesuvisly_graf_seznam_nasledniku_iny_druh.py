from collections import deque
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
				#0       #1        #2   #3   #4  #5  #6
graph2.succs = [[2], [1, 0, 4, 2], [1], [1], [], [6], [5]]

# Toto je nesuvisly graf

def mainBFS(graph, vertex, visited, path):
	queue = deque()
	visited[vertex] = True
	queue.append(vertex)

	while queue:
		currentVertex = queue.popleft()
		path.append(currentVertex)

		for ver in graph.succs[currentVertex]:
			if (visited[ver] == False):
				queue.append(ver)
				visited[ver] = True

def startingBFS(graph):
	visited = [False] * graph.size
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

print(startingBFS(graph2))
# Musis si to trosku upravit pre tento typ reprezentacie
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


