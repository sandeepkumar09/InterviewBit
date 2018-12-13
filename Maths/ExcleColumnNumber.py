
class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        res = 0
        for char in A:
            diff = ord(char) - ord('A') + 1
            #print(ord(A), diff)
            res = res * 26 + diff

        return res

sol = Solution()
print(sol.titleToNumber("BA"))