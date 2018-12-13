class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSum(self, A):
        A.sort()
        res = set()
        temp = []
        res_set = []
        for i in range(len(A)):
            target = A[i]
            j = i+1
            k = len(A) - 1
            while j < k and j < len(A):
            	if A[j] + A[k] + target == 0:
            		res.add((A[i], A[j], A[k]))
            	if A[j] + A[k] + target > 0:
            		k -= 1
            	else:
            		j += 1
        return list(res)
sol = Solution()
print(sol.threeSum([-1 ,0 ,1, 2 ,-1 ,-4]))