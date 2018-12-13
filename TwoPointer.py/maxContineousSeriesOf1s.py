class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
    	i, j = 0, 0
    	x, y = 0, 0
    	while j < len(A):
    		if A[j]:
    			if y - x < j - i:
    				y, x = j, i
    			j += 1
    		elif not A[j] and B > 0:
    			if y - x < j - i:
    				y, x = j, i
    			B -= 1
    			j += 1
    		else:
    			if not A[i]:
    				B += 1
    			i += 1
    	return list(range(x, y+1))
sol = Solution()
print(sol.maxone([1 ,1, 0, 1, 1, 0,0, 1, 1, 1], 1))