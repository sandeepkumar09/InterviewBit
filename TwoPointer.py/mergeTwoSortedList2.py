class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
    	i = 0
    	j = 0
    	C = []
    	a = 0
    	while True:
    		if i >= len(A) and j >= len(B):
    			break
    		if i == len(A):
    			C.append(B[j])
    			j += 1
    		elif j == len(B):
    			C.append(A[i])
    			i += 1
    		elif A[i] > B[j]:
    			C.append(B[j])
    			j += 1
    		else:
    			C.append(A[i])
    			i += 1
    	return C
sol = Solution()
f = [3]
f.extend([4,5])
print(f)
print(sol.merge([-4,3], [-2,-2]))