class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
    	num = len(A)
    	diff = 0
    	diff_sqr = 0
    	# actual_sumition = 0
    	# actual_sqr_sumition = 0
    	#expected_sumition = num*(num+1)/2
    	#expected_sqr_sumition = num*(num+1)*(2*num +1)/6
    	for i in range(len(A)):
    		diff += (i+1) - A[i]
    		diff_sqr += (i+1)*(i+1)-A[i]*A[i]
    	# diff_sumition = expected_sumition - actual_sumition
    	# diff_sqr_sumition = expected_sqr_sumition -actual_sqr_sumition
    	# miss = ((diff_sqr_sumition/diff_sumition)+diff_sumition)/2
    	miss = ((diff_sqr/diff)+ diff)/2
    	dupl = miss - diff
    	print([dupl, miss])
    	return [dupl, miss]

sol = Solution()
sol.repeatedNumber([2,1,1])

