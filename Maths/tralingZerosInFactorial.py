class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
    	count = 0
    	i = 5
    	while A/i >= 1:
    		count += int(A/i)
    		i *= 5
    	return count
sol = Solution()
print(sol.trailingZeroes())