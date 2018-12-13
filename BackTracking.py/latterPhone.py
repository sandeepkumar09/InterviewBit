class Solution:
    MAP = {
        '0': '0',
        '1': '1',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        }

    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        A = list(A)
        ans, temp = [], []
        self.helper(ans,temp,A, 0)
        ans.sort()
        return ans
    def helper(self, ans,temp, number, curr_digit):
        if curr_digit == len(number):
            ans.append(''.join(temp))
        else:
            for i in range(len(self.MAP[number[curr_digit]])):
                temp.append(self.MAP[number[curr_digit]][i])
                self.helper(ans, temp, number, curr_digit+1)
                temp.pop()

sol = Solution()
print(sol.letterCombinations('23'))
