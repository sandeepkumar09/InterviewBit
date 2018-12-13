class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
    	ans = 0
    	for i in range(32):
    		count = 0
    		for element in A:
    			count += element & (1 << i) > 0
    		ans += (count *(len(A) - count) * 2) % 1000000007
    	return ans % 1000000007
sol = Solution()
print(sol.cntBits([1, 3, 5]))