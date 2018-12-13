class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
    	B =[0 for i in range(A)]
    	C = [0 for i in range(A)]
    	# for i in range(A):
    	# 	for j in range(i+1):
    	# 		B for i in range(A):
    	B[0] = 1
    	C[0] = 1
    	flag = False
    	#print(B)
    	for i in range(A):
    		for j in range(i+1):
    			if i % 2 != 0:
	    			if j != 0 and j != i:
	    				# print(j)
	    				# print("aaa")
	    				#print(B[i][j],B[i-1][j-1],B[i-1][j])
	    				#B[i][j] = B[i-1][j-1] + B[i-1][j]
	    				B[j] = C[j-1]+C[j]
	    			elif j == 0:
	    				B[j] = C[j]
	    			else:
	    				B[j] = C[j-1]
	    		else:
	    			if j != 0 and j != i:
	    				# print(j)
	    				# print("aaa")
	    				#print(B[i][j],B[i-1][j-1],B[i-1][j])
	    				#B[i][j] = B[i-1][j-1] + B[i-1][j]
	    				C[j] = B[j-1]+B[j]
	    			elif j == 0:
	    				C[j] = B[j]
	    			else:
	    				C[j] = B[j-1]
    	if A %2 == 0:
    		print(B,"bb")
    		return B
    	else:
    		print(C)
    		return C
    	return B


sol = Solution()
sol.generate(3)