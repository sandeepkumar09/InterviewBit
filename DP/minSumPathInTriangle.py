class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
    	if not A:
    		return 0
    	n = len(A)
    	m = len(A[-1])
    	depth = 1
    	self.visited = [[0 for i in range(j+1)] for j in range(n)]
    	self.dp = [[0 for i in range(j+1)] for j in range(n)]
    	return self.Pathsum(0, 0, n, m, A, self.visited, self.dp, depth)
    def Pathsum(self, i, j ,n, m, arr, visited, dp, depth):
    	if visited[i][j] == 1:
    		return dp[i][j]
    	visited[i][j] = 1
    	if i == n-1:
    		#return arr[i][j]
    		dp[i][j] = arr[i][j]
    	# elif i == n-1:
    	# 	#return arr[i][j]+self.Pathsum(i, j+1, n, m, arr, visited, dp)
    	# 	dp[i][j] = arr[i][j]+self.Pathsum(i, j+1, n, m, arr, visited, dp, depth)
    	# elif j == depth-1:
    	# 	#return arr[i][j]+self.Pathsum(i+1,j, n, m, arr, visited, dp)
    	# 	dp[i][j] = arr[i][j]+self.Pathsum(i+1,j, n, m, arr, visited, dp, depth)
    	else:
    		#return arr[i][j]+min(self.Pathsum(i+1, j, n, m, arr, visited, dp), self.Pathsum(i, j+1, n, m, arr, visited, dp))
    		dp[i][j] = arr[i][j]+min(self.Pathsum(i+1, j, n, m, arr, visited, dp, depth+1), self.Pathsum(i+1, j+1, n, m, arr, visited, dp, depth+1))
    	return dp[i][j]
sol = Solution()
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))