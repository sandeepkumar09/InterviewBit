class Solution:
    # @param A : string
    # @return a list of list of strings
    def isPallindrome(self, arr, start, end):
        while start < end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True
    def partition(self, A):
        A = list(A)
        ans = []
        temp = []
        self.helper(ans, A, temp, 0)
        ans.sort()
        return ans
    def helper(self,ans, arr, temp, left):
        if left >= len(arr):
            print(temp)
            ans.append([j for j in temp])
        else:
            for i in range(left, len(arr)):
                if self.isPallindrome(arr, left, i):
                    temp.append(''.join([arr[j] for j in range(left, left+i-left+1)]))
                    self.helper(ans,arr, temp, i+1)
                    temp.pop()
sol = Solution()
print(sol.partition('aab'))
