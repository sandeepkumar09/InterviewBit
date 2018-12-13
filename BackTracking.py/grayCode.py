class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        self.ans = []
        self.num = 0
        self.helper(self.ans, A, self.num)
        return self.ans
    def helper(self, ans, n, num):
        if n == 0:
            self.ans.append(self.num)
        else:
            self.helper(self.ans, n-1, self.num)
            self.num = self.num^(1 <<(n-1))
            self.helper(self.ans, n-1, self.num)
sol = Solution()
print(sol.grayCode(3))
