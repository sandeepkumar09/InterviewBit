# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
    	res = []
    	stack = []
    	curr = A
    	while curr or stack:
    		while curr:
    			stack.append(curr)
    			curr = curr.left
    		curr = stack.pop()
    		temp = curr.right
    		#res.append(curr.val)
    		curr.left, curr.right = curr.right, curr.left
    		curr = temp
    	return A