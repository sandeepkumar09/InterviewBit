class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
    	start = 0
    	end = len(A) - 1
    	while start <= end:
    		if A[mid] == B:
    			return mid
    		elif A[mid] <= A[end]:
    			if B > A[mid] and B <= A[end]:
    				start = mid + 1
    			else:
    				end = mid - 1
    		elif A[start] <= A[mid]:
    			if B > A[start] and B <= A[mid]:
    				end = mid - 1
    			else:
    				start = mid + 1
sol = Solution()
print(sol.search())