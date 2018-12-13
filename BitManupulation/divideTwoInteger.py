class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
    	if A < B :
    		return 0
    	ans = 0
    	print(5^2)
    	while A >= B:
    		A ^= B
    		ans += 1
    		print(ans)
    	return ans
sol = Solution()
print(sol.divide(5,5))