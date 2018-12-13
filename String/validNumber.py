class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
    	A = A.split()
    	for i in range(len(A)):
    		if A[i].isdigit() != True or A[i] == 'e':
    			if A[i] == 'e' and A[i+1].isdigit() != True and A[i+1] <= 1:
    				return 0
    			return 1
    		else:
    			return 1
sol = Solution()	
print(sol.isNumber('123e45'))