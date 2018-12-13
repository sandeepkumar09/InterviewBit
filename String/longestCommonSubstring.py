class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
    	n = len(A):
    	dp = [[False for i in range(n)] for j in range(n)]
    	maxLength = 1
    	i = 0
    	# substring of length 1 are palindrome
    	while (i < n):
    		dp[i][i] = True
    		i += 1
    	# check for substring of length = 2
    	start = 0
    	for i in range(1, n):
    		if A[i] == A[i-1]:
    			dp[i-1][i] = True
    			if maxLength < 2:
    				maxLength = 2
    				start = i - 1
    	# check for substing of length >= 3
    	for k in range(3, n-1):
    		for i in range(n + 1 - k):
    			if 