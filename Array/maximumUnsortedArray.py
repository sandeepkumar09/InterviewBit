class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        mini = 100000
        maxi = -1
        ans = []
        maxEle = -1
        flag = True
        minEle = 1000000
        for i in range(1,len(A)):
            if A[i] < A[i-1] or maxEle > A[i]:
            	maxEle = max(maxEle, A[i-1],A[i])
            	minEle = min(minEle,A[i-1],A[i])
            	mini = min(mini, i-1)
            	maxi = max(maxi, i)
            	flag = False
        for i in range(len(A)):
        	if minEle < A[i] and mini > i:
        		mini = i
        if flag:
            return [-1]
        ans.append(mini)
        ans.append(maxi)
        return ans
sol = Solution()
print(sol.subUnsort([1, 2, 3, 5, 6, 13, 15, 16, 17, 13, 13, 15, 17, 17, 17, 17, 17, 19, 19 ]))