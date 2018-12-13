# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
		res = []
		stack = []
		curr = A
		while curr or stack:
			while curr:
				stack.append(curr)
				curr = curr.left
			curr = stack.pop()
			res.append(curr.val)
			curr = curr.right
		return res