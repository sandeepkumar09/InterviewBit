class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
    	row =[]
    	col =[]
    	for i in range(len(A)):
    		for j in range(len(A[0])):
    			if A[i][j] == 0:
    				row.append(i)
    				col.append(j)
    	for i in set(row):
    		for j in range(len(A[0])):
    			A[i][j] = 0
    	for i in set(col):
    		for j in range(len(A)):
    			A[j][i] = 0
    	return A
sol = Solution()
print(sol.setZeroes([[1, 0, 1], [1, 1, 1], [1, 1, 1]]))
