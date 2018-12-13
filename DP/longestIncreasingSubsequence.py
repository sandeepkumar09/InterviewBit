class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
    	max_ = 0
        dp = [1 for i in A]
    	#dp = [[0 for i in A] for j in A]
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i] < A[j]:
                    dp[j] = max(dp[i]+1, dp[j])
                max_ = max(max_, dp[j])
        # for i in range(1,len(A)):
        #     for j in range(0,i):
        #         if A[j] < A[i]:
        #             dp[i] = max(dp[j] + 1, dp[i])
        #             max_ = max(max_, dp[i])
        print(dp)
        return max_
sol = Solution()
print(sol.lis([0,8,4,12,6]))
# print(sol.lis([0, 8, 4, 12, 2, 10, 6]))
# print(sol.lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(sol.lis([14, 24, 18, 46, 55, 53, 82, 18, 101, 20, 78, 35, 68, 9, 16, 93, 101]))
#[1, 2, 2, 3, 4, 4, 5, 2, 6, 3, 5, 4, 5, 1, 2, 6, 7]
#print(sol.lis( [ 14, 24, 18, 46, 55, 53, 82, 18, 101, 20, 78, 35, 68, 9, 16, 93, 101, 85, 81, 28, 78 ]))