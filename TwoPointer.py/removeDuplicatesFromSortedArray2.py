class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
    	i = 0
    	while i < len(A) - 2:
    		j = i + 2
    		while j < len(A) and A[i] == A[i + 1] and A[i] == A[j]:
    			j += 1
    		A[i+2: j] = []
    		i += 1
    	print(A)
    	return len(A)
sol = Solution()
print(sol.removeDuplicates([]))