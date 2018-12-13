class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):
		if A is None:
			return []
		res = []
		stack1 = []
		stack2 = []

		stack1.append(A)

		while stack1:
			curr = stack1.pop()
			stack2.append(curr)
			if curr.left:
				stack1.append(curr.left)
			if curr.right:
				stack1.append(curr.right)
		while stack2:
			curr = stack2.pop()
			res.append(curr.val)
		return res