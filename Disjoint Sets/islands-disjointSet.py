#Number of islands using disjoint sets
class DisjointUnionSets:
	def __init__(self, n):
		self.rank = [0] * n
		self.parent = [0] * n
		self.n = n
		self.makeSet()

	def makeSet(self):
		
		for i in range(self.n):
			self.parent[i] = i

	def find(self, x):
		if (self.parent[x] != x):

			self.parent[x]=self.find(self.parent[x])
			
		return self.parent[x]

	def Union(self, x, y):
		
		xRoot = self.find(x)
		yRoot = self.find(y)

		if xRoot == yRoot:
			return

		if self.rank[xRoot] < self.rank[yRoot]:
			parent[xRoot] = yRoot

		elif self.rank[yRoot] < self.rank[xRoot]:
			self.parent[yRoot] = xRoot

		else:
			
			self.parent[yRoot] = xRoot

			self.rank[xRoot] = self.rank[xRoot] + 1

def countIslands(a):
	n = len(a)
	m = len(a[0])

	dus = DisjointUnionSets(n * m)

	for j in range(0, n):
		for k in range(0, m):

			if a[j][k] == 0:
				continue

			if j + 1 < n and a[j + 1][k] == 1:
				dus.Union(j * (m) + k,
						(j + 1) * (m) + k)
			if j - 1 >= 0 and a[j - 1][k] == 1:
				dus.Union(j * (m) + k,
						(j - 1) * (m) + k)
			if k + 1 < m and a[j][k + 1] == 1:
				dus.Union(j * (m) + k,
						(j) * (m) + k + 1)
			if k - 1 >= 0 and a[j][k - 1] == 1:
				dus.Union(j * (m) + k,
						(j) * (m) + k - 1)
			if (j + 1 < n and k + 1 < m and
					a[j + 1][k + 1] == 1):
				dus.Union(j * (m) + k, (j + 1) *
							(m) + k + 1)
			if (j + 1 < n and k - 1 >= 0 and
					a[j + 1][k - 1] == 1):
				dus.Union(j * m + k, (j + 1) *
							(m) + k - 1)
			if (j - 1 >= 0 and k + 1 < m and
					a[j - 1][k + 1] == 1):
				dus.Union(j * m + k, (j - 1) *
							m + k + 1)
			if (j - 1 >= 0 and k - 1 >= 0 and
					a[j - 1][k - 1] == 1):
				dus.Union(j * m + k, (j - 1) *
							m + k - 1)

	c = [0] * (n * m)
	numberOfIslands = 0
	for j in range(n):
		for k in range(n):
			if a[j][k] == 1:
				x = dus.find(j * m + k)
				
				if c[x] == 0:
					numberOfIslands += 1
					c[x] += 1
				else:
					c[x] += 1
	return numberOfIslands

a = [[1, 1, 0, 0, 0],
	[0, 1, 0, 0, 1],
	[1, 0, 0, 1, 1],
	[0, 0, 0, 0, 0],
	[1, 0, 1, 0, 1]]
print("Number of Islands is:", countIslands(a))

#Output: the number of islands is: 5

