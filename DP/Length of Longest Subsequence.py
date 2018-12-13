class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
    	if not A:
    		return 0
    	max_ = 0
    	dp_increasing = [1 for i in A]
    	dp_decreasing = [1 for i in A]
        for i in range(1,len(A)):
            for j in range(0,i):
                if A[j] < A[i]:
                    dp_increasing[i] = max(dp_increasing[j] + 1, dp_increasing[i])
                    #max_ = max(max_, dp_increasing[i])
        B = [i for i in reversed(A)]
        for i in (range(1,len(B))):
            for j in range(0,i):
                if B[j] < B[i]:
                    dp_decreasing[i] = max(dp_decreasing[j] + 1, dp_decreasing[i])
                    #max_ = max(max_, dp[i])
    	# for i in (range(len(A))):
    	# 	for j in range(i,len(A)):
    	# 		if i == j:
    	# 			dp_decreasing[i][j] = 1
    	# 		elif A[i] > A[j]:
    	# 			dp_decreasing[i][j] = 1+dp_decreasing[i][i]
    	# 		dp_decreasing[i][j] = max(dp_decreasing[i][j], dp_decreasing[i-1][j],1) # focus on i = 0 and dp_increasing[i-1][j]
        print(dp_increasing)
        print(dp_decreasing)
        for i in range(len(A)):
            max_ = max(max_, dp_increasing[i]+ (dp_decreasing[len(A)-i-1])-1)
        return max_
sol = Solution()
print(sol.longestSubsequenceLength([ 1, 11, 2, 10, 4, 5, 2, 1 ]))
print(sol.longestSubsequenceLength([ 1, 3, 5, 6, 4, 8, 4, 3, 2, 1 ]))