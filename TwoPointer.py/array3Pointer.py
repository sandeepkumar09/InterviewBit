import sys
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
    	p, q, r = len(A), len(B), len(C)
    	diff = sys.maxsize
    	res_i = 0
    	res_j = 0
    	res_k = 0
    	# Travesre Array
    	i = 0
    	j = 0
    	k = 0
    	while i < p and j < q and k < r:
    		minimum = min(A[i], min(B[j], C[k]))
    		maximum = max(A[i], max(B[j], C[k]))
    		if maximum - minimum < diff:
    			res_i = i
    			res_j = j
    			res_k = k
    			diff = maximum - minimum
    		if diff == 0:
    			break
    		if A[i] == minimum:
    			i += 1
    		elif B[j] == minimum:
    			j += 1
    		else:
    			k += 1
    	return (abs(A[res_i]-B[res_j]) + abs(B[res_j]- C[res_k]) + abs(C[res_k]- A[res_i]))