class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
    	B =[[1 for a in range(b+1)] for b in range(A)]
    	# for i in range(A):
    	# 	for j in range(i+1):
    	# 		B for i in range(A):
    	print(B)
    	for i in range(A):
    		for j in range(i+1):
    			if j != 0 and j != i:
    				# print(j)
    				# print("aaa")
    				#print(B[i][j],B[i-1][j-1],B[i-1][j])
    				B[i][j] = B[i-1][j-1] + B[i-1][j]
    	print(B)
    	return B




sol = Solution()
sol.generate(3)