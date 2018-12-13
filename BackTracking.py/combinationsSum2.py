class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        ans, temp = [], []
        self.helper(ans, temp, A, B, 0)
        ans.sort()
        for i in range(len(ans)):
            if not temp or ans[i] != temp[-1]:
                temp.append(ans[i])
        return temp
    def helper(self, ans, temp, A, B, left):
        if sum(temp) >= B:
            if sum(temp) == B:
                ans.append([j for j in temp])
        else:
            for i in range(left, len(A)):
                temp.append(A[i])
                self.helper(ans, temp, A, B, i+1)
                temp.pop()
sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))
