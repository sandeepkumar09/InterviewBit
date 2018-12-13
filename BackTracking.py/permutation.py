class Solution():
    # @param A : list of intergers
    # @param B : integer
    # @return a list of list of intergers
    def permute(self, A):
        ans = []
        temp = []
        self.helper(ans, temp, A, 0)
        ans.sort()
        return ans
    def helper(self, ans, temp, A, left,):
        if left == len(A):
            ans.append([j for j in A])
        else:
            for i in range(left, len(A)):
                A[left], A[i] = A[i], A[left]
                #temp.append(A[i])
                self.helper(ans, temp, A, left+1)
                #temp.pop()
                A[left], A[i] = A[i], A[left]
sol = Solution()
print(sol.permute([1,2,3]))
