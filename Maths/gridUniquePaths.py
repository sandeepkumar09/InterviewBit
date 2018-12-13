class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def fact(self, N, X):
    	fact = 1
    	for i in range(N , 0, -1):
    		if i == X:
    			break
    		fact *= i
    	return fact
    def uniquePaths(self, A, B):
    	if A < B:
    		A, B = B, A
    	c = self.fact(B-1, 1)
    	a = self.fact(A+B-2, A-1)
    	return a//(c)
sol = Solution()
print(sol.uniquePaths(1,3000))