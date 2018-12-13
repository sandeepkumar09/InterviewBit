class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
    	for i in range(len(A)):
    		if A[i] == 0 and i != 0:
    			A[i:i+1] = []
    			A.insert(0, 0)
    		elif A[i] == 2 and i != len(A)-1:
    			A[i:i+1] = []
    			A.append(2)
    		else:
    			pass
    	return A
sol = Solution()
a = [0,1,2]
a[0:1] = []
a.insert(0,0)
print(a)
print(sol.sortColors([1,0,2,1]))