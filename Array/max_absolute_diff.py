class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
    	# max_diff = 0
    	# for i in range(len(A)):
    	# 	for j in range(i,len(A)):
    	# 		diff = max(A[i]-A[j], A[j]-A[i]) + max(i-j, j-i)
    	# 		max_diff = max(max_diff,diff)
    	# print(max_diff)
    	# return max_diff
    	max1 = -2147483648
    	min1 = +2147483647
    	max2 = -2147483648
    	min2 = +2147483647
    	for i in range(len(A)):
    		max1 = max(max1, A[i]+i)
    		min1 = min(min1, A[i]+i)
    		max2 = max(max2, A[i]-i)
    		min2 = min(min2, A[i]-i)
    	print (max(max1-min1, max2-min2))
    	return max(max1- min1, max2- min2)


sol = Solution()
sol.maxArr([1,3,-1])