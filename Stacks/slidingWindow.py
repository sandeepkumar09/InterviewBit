class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        result = []
        window = []
        if B > len(A):
            B = len(A)
        for i in range(len(A)-3):
            window = A[i: i+B-1]
            result.append(max(window))
        return result
