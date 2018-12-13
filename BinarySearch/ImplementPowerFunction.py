class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
    	if x == 0:
    		return 0
    	if n == 0:
    		return 1
    	elif n % 2 == 1:
    		return (x*self.pow(x, n-1, d)) %d
    	else:
    		return (self.pow(x, n//2, d)**2) %d
sol = Solution()
print(sol.pow(2, 3, 3))

