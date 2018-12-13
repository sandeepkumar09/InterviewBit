class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        ans = []
        subset = [None for j in A]
        self.helper(A, subset, 0,ans)
        # for i in range(0,len(ans)-1):
        #     for j in range(1, len(ans)-i-1):
        #         for k in range(0, min(len(ans[j]), len(ans[j+1]))):
        #             if ans[j][k] > ans[j+1][k]:
        #                 ans[j], ans[j+1] = ans[j+1], ans[j]
        #                 break
        ans.sort()
        return ans
    def helper(self, A, subset, i, ans):
        if i == len(A):
            ans.append([j for j in subset if j is not None])
            #ans.sort()
            # hole = len(ans)-1
            # n = len(ans)-1
            # key = ans[n]
            # for j in range(n-1, 0, -1):
            #     for k in range(0, min(len(ans[j]), len(key))):
            #         if ans[j][k] > key[k]:
            #             ans[j+1], hole = ans[j], j
            #             break
            #     else:
            #         break
            # ans[hole] = key
        else:
            subset[i] = None
            self.helper(A, subset, i+1,ans)
            subset[i] = A[i]
            self.helper(A, subset, i+1, ans)
sol = Solution()
print(sol.subsets( [ 15, 20, 12, 19, 4 ]))
print(sol.subsets([1,2,3,4]))
