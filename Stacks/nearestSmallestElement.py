class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
    	G = [0 for i in A]
    	stack = []
    	i = 0
    	while i <= len(A):
    		print(stack, i)
    		if not stack or (i < len(A) and A[stack[-1]] < A[i]):
    			stack.append(i)
    			i += 1
    		else:
    			last = stack.pop()
    			if stack:
    				G[last] = A[stack[-1]]
    			else:
    				G[last] = -1
    	return G

sol = Solution()
print(sol.prevSmaller( [ 1 ]))