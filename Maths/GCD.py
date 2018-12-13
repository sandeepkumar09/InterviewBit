class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
    	if A < B:
    		A, B = B, A
    	while True:
    		reminder = A % B
    		if reminder == 0:
    			return B
    		A = B
    		B = reminder
    	return 0
sol = Solution()
print(sol.gcd(6, 1))