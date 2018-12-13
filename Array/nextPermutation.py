class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
    	temp = A[-1]
    	for i in range(len(A)-1 , 0, -1):
    		if float(A[i-1]/A[i]) < 1:
    			A[i], A[i-1] = A[i-1], A[i]
    			print(A)
    			print(int((len(A)-i)/2),i)
    			rge = len(A)-i
    			print(len(A)-i,"ss")
    			for j in range(int(rge/2)):
    				A[i+j], A[len(A)-1-j] = A[len(A)-1-j], A[j+i]
    			return A
    	A.sort()
    	return A
sol = Solution()
print(sol.nextPermutation([319, 695, 52 ,11,9]))
print(sol.nextPermutation([59, 854, 422]))
# 319, 695, 52
# 695, 319, 52
# 695, 523, 19