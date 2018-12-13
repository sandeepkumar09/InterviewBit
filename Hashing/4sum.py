class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        res = []
        A.sort()
        for i in range(len(A)):
            if i >= 1 and A[i] == A[i-1]:
                continue
            for j in range(i+1, len(A)):
                if j >= 1 and A[j] == A[j-1]:
                    continue
                a = A[i]
                b = A[j]
                k = j+1
                l = len(A)-1
                while k < l:
                    if (k >= 3 and A[k] == A[k-1]) or (l >= 3 and A[l] == A[l-1]):
                        continue
                    _sum = a + b + A[k] + A[l]
                    if _sum == B:
                        res.append([a, b, A[k], A[l]])
                    elif _sum < B:
                        k += 1
                    else:
                        l -= 1
        return res
