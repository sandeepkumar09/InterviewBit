class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
    	A = sorted(A)
    	print(A)
    	_min = float('INF')
    	for i in range(len(A)):
    		target = B - A[i]
    		j = i+1
    		k = len(A) - 1
    		while j < k and j < len(A):
    			if _min > abs(target - A[j] - A[k]):
    				_min = abs(target - A[j] - A[k])
    				res = A[i] + A[j] + A[k]
    			if A[j] + A[k] == target:
    				return B
    			if A[j] + A[k] > target:
    				k -= 1
    			else:
    				j += 1
    	return res
sol = Solution()
print(sol.threeSumClosest([-1 ,2 ,1 ,-4],1))