













class Queue:
	def __init__(self):
		self.data = []

	def enqueue(self, value):
		self.data.append(value)

	def dequeue(self):
		return self.data.pop(0)

	def isEmpty(self):
		return len(self.data) == 0

def BFS(start, successors, goals):
	q = Queue()
	parent = {}
	parent[start] = None
	q.enqueue(start)
	while not q.isEmpty():
		node = q.dequeue()
		if node in goals:
			break
		for successor in successors(node):
			if successor not in parent:
				parent[successor] = node
				q.enqueue(successor)
		node = None

	res = []
	while node is not None:
		res.append(node)
		node = parent[node]
		print(parent)

	return list(reversed(res))

def successors(node):
	laby = [
		"##########",
		"#        E",
		"# # ######",
		"# #      #",
		"# # # ####",
		"#####    #",
		"#   # ####",
		"# # # #  #",
		"# #      #",
		"##########",
	]

	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	res = []
	l, c = node
	for dl, dc in directions:
		nl = l + dl
		nc = c + dc
		if laby[nl][nc] in [' ', 'E']:
			res.append((nl, nc))
	print(res)
	return res

print(BFS((8, 1), successors, [(1, 9)]))