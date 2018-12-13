class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
    	halflength = int(len(A)/2)
    	for i in range(halflength):
    		if A[i] != A[len(A)-i-1]:
    			return 0
    	return 1