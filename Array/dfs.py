from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	def addEdge(self, lastNode, newNode):
		self.graph[lastNode].append(newNode)
	def dfs_Until(self, newNode, visitedNodes):
		visitedNodes[newNode] = True
		print (newNode)
		for i in self.graph[v]:
			if visitedNodes[i] == False:
				self.dfs_Until(i, visitedNodes)
	def DFS(self,newNode):
		visitedNodes = [False]*(len(self.graph))
		self.dfs_Until(newNode,visitedNodes)
