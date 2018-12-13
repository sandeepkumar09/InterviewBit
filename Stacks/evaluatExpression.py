class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
    	stack = []
    	for a in A:
    		if a in ['+', '-', '*', '/']:
    			right = stack.pop()
    			left = stack.pop()
    			res = eval('int({}{}{})'.format(right, a, left))
    			stack.append(res)
    		else:
    			stack.append(a)
    	return stack.pop()