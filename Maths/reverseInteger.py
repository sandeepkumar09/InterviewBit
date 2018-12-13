class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
    	B = ""
    	if A < 0:
    		A *= -1
    		A = str(A)
    		for i in range(len(A)-1, -1, -1):
    			B += A[i]
    		if int(B) > (2**31):
    			return 0
    		return int(B)*(-1)
    	A = str(A)
    	for i in range(len(A)-1, -1, -1):
    		B += A[i]
    	if int(B) > (2**31):
    		return 0
    	return int(B)
sol = Solution()
print(sol.reverse(-1153072433))
print(2**32)