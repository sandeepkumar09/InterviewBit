class Solution:
	# @param A : tuple of integers
	# @return an integer
	def counting_sort(self,array1, max_val):
	    m = max_val + 1
	    count = [0] * m                
	    
	    for a in array1:
	    # count occurences
	        count[a] += 1             
	    i = 0
	    for a in range(m):            
	        for c in range(count[a]):  
	            array1[i] = a
	            i += 1
	    return array1
	#Sort takes close to linear time
	def maximumGap(self, A):
		A = self.counting_sort(A, max(A))
		maximum = -1
		for i in range(len(A)-1):
			maximum = max(maximum, int(A[i+1])-int(A[i]))
		if maximum == -1:
			return 0
		return maximum
sol = Solution()
print(sol.maximumGap([])