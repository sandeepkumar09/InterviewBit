class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
    	sum_arr = 0
    	max_sum = 0
    	for i in range(len(A)):
    		sum_arr = sum_arr + A[i]
    		if sum_arr < 0:
    			sum_arr = 0
    		max_sum = max(max_sum, sum_arr)
    	if max_sum == 0:
    		max_sum = max(A)
    		print(max_sum)
    	return max_sum


sol = Solution()

sol.maxSubArray([-1])