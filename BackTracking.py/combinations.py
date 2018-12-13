class Solution():
    # @param A : integer
    # @param B : integer
    # @return a list of list of intergers
    def combine(self, A, B):
        ans = []
        temp = []
        self.helper(ans, temp, A , 1, B)
        ans.sort()
        return ans
    def helper(self, ans, temp, n, left, k):
        if k == 0:
            ans.append([j for j in temp])
        else:
            for i in range(left, n+1):
                temp.append(i)
                self.helper(ans, temp, n, i+1, k-1)
                temp.pop()
sol = Solution()
print(sol.combine(4,2))
