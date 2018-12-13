class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
    	integers = [0 for i in range(B)]
    	largest = B
    	smallest = 1
    	for i in range(len(A)):
    		if A[i] == 'D':
    			#print('dd')
    			integers[i] = largest
    			largest -= 1
    		else:
    			#print('ss')
    			integers[i] = smallest
    			smallest += 1
    	#print(largest,i,len(A))
    	integers[i+1] = largest
    	return integers
sol = Solution()
print(sol.findPerm('IDDI', 5))