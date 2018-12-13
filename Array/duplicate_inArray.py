class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
    	B =[0 for i in A]
    	for i in range(len(A)):
    		if B[A[i]] == 0:
    			B[A[i]] = 1
    		else:
    			return A[i]
    	return -1
sol = Solution()
print(sol.repeatedNumber([3,1,4,4,1]))