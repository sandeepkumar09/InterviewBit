class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
    	i = 0
    	while i < len(A):
    		j = i
    		while j < len(A) and A[j] == B:
    			j += 1
    		A[i:j] = []
    		i += 1
    	return len(A)
sol = Solution()
print(sol.removeElement([3,1,1,1,1,2],1))