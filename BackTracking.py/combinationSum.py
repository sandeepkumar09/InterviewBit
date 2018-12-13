class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A = set(A)
        A = [i for i in A]
        ans, temp = [], []
        self.helper(ans, temp, A, B, 0)
        return sorted(ans)
    def helper(self, ans, temp, A, B, left):
        if sum(temp) >= B:
            if sum(temp) == B:
                ans.append([j for j in temp])
        else:
            for i in range(left, len(A)):
                temp.append(A[i])
                self.helper(ans, temp, A, B, i)
                temp.pop()
sol = Solution()
print(sol.combinationSum([2,2,3,6,7], 7))
