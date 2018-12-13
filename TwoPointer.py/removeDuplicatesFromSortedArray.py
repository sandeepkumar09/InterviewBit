class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 0
        while i < len(A) - 1:
            j = i + 1
            while j < len(A) and A[i] == A[j] :
                j += 1
            A[i + 1:j] = []
            i += 1
        return len(A)
sol = Solution()
print(sol.removeDuplicates([0]))
print(sol.removeDuplicates([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]))