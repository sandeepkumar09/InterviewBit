class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
    	ones = 0
    	twos = 0
    	for i in range(len(A)):
    		twos = twos | (ones & A[i])
    		ones = ones ^ A[i]
    		common_bit_mask = ~(ones & twos)
    		ones &= common_bit_mask
    		twos &= common_bit_mask
    	return ones
sol = Solution()
print(sol.singleNumber( [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]))
