class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
    	last = A
    	first = 0
    	while first < last:
    		middle = ((first + last) // 2) + first
    		#print(middle)
    		if middle**2 <= A and (middle+1)**2 > A:
    			return int(middle)
    		elif (middle+1)**2 < A:
    			first = middle + 1
    		else:
    			last = middle - 1
    	return last
sol = Solution()
print(sol.sqrt(2))