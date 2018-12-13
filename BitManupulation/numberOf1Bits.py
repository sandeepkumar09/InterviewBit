class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
    	count = 0
    	while A:
    		print(A)
    		A &= A - 1
    		print(A)
    		count += 1
    	return count
sol = Solution()
print(sol.numSetBits(45))