class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
    	n = len(A)
    	dp = [[0 for i in range(n)] for j in range(n)]
    	maxLength = 0
    	# check substring of length 1
    	for i in range(n):
    		dp[i][i] = 1
    	maxLength = 1
    	start = 0
    	#print(dp)
    	# check for substring of length 2
    	for i in range(1,n):
    		if A[i] == A[i-1]:
    			print(dp)
    			dp[i][i-1] = 1
    			if maxLength < 2:
    				maxLength = 2
    				start = i-1
    	print(dp)
    	#check for substring of length of 3 or more
    	for k in range(3,n):
    		for i in range(n + 1 - k):
    			j = i + k - 1
    			print(dp)
    			if dp[i+1][j-1] and A[i] == A[j]:
    				dp[i][j] = 1
    				if maxLength < k:
    					maxLength = k
    					start = i - j
    	return maxLength
sol = Solution()
print(sol.longestPalindrome('abcbc'))