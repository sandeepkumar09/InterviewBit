class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
    	stack = []
    	for a in A:
    		if a == ')' and (stack.pop() == '(' or stack.pop() == '('):
    			return 1
    		elif a == ')':
    			while(stack):
    				if stack.pop() == '(':
    					break
    		else:
    			stack.append(a)
    	return 0
sol = Solution()
print(sol.braces('(a)'))

