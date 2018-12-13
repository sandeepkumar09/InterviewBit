class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
    	A = A.split('.')
    	B = B.split('.')
    	if len(A) < len(B):
    		for i in range(len(B)-len(A)):
    			A.append('0')
    	if len(B) < len(A):
    		for i in range(len(A)-len(B)):
    			B.append('0')
    	for i in range(len(A)):
    		if int(A[i]) > int(B[i]):
    			return 1
    		if int(A[i]) < int(B[i]):
    			return -1
    	return 0
sol = Solution()
print(sol.compareVersion('01', '1.0.0.0'))