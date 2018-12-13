class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
    	if not A:
    		return 0
    	n = len(A)
    	m = len(A[0])
    	dp = [[0 for i in range(m)] for j in range(n)]
    	if A[0][0] == 1:
    		return 0
    	dp[0][0] = 1
    	for i in range(n):
    		for j in range(m):
    			if A[i][j] == 1:
    				continue
    			if i-1 >= 0 and j-1 >= 0:
    				dp[i][j] = dp[i-1][j]+dp[i][j-1]
    			elif i-1 >= 0:
    				dp[i][j] = dp[i-1][j]
    			elif j-1 >= 0:
    				dp[i][j] = dp[i][j-1]
    	#print(dp)
    	return dp[n-1][m-1]

sol = Solution()
print(sol.uniquePathsWithObstacles([[1,0]]))