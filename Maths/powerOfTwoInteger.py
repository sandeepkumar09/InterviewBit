class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
    	for i in range(1, int(A**0.5)+2):
    		for j in range(2, int(A**0.5)+2):
    			if i**j > A:
    				break
    			if i**j == A:
    				return 1
    	return 0
sol = Solution()
print(sol.isPower(1024000000))