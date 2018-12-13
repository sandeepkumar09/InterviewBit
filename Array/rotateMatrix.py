class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
    	for i in range(len(A)):
    		for j in range(i,len(A)):
    			A[i][j], A[j][i] = A[j][i], A[i][j]
    	for i in range(len(A)):
    		for j in range(int(len(A)/2)):
    			A[i][j], A[i][len(A)-j-1] = A[i][len(A)-j-1], A[i][j]
    	return A

sol = Solution()
print(sol.rotate([[1, 2], [3, 4]]))
print(sol.rotate([[1, 2,3], [4,5,6], [7,8,9]]))