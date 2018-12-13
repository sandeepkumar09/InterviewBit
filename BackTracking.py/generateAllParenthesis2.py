class Solution:
    # @param A : integer
    # @return a list of strings
    def isWellFormParentheses(self, arr, n,k):
        count = 0
        stack = []
        for i in range(k):
            if arr[i] == ')':
                if not stack:
                    return False
                else:
                    stack.pop()
            else:
                count += 1
                stack.append('(')
        if count > n:
            return False
        return True
    def generateParenthesis(self, A):
        ans, temp = [], [0 for i in range(2*A)]
        self.helper(A, temp, 0, ans)
        ans.sort()
        return ans
    def helper(self, A, temp, i, ans):
        if i >= 2*A and self.isWellFormParentheses(temp, A, 2*A):
            ans.append(''.join([j for j in temp]))
        else:
            if self.isWellFormParentheses(temp, A, i):
                temp[i] = '('
                self.helper(A, temp, i+1, ans)
                temp[i] = ')'
                self.helper(A, temp, i+1, ans)
sol = Solution()
print(sol.generateParenthesis(3))
