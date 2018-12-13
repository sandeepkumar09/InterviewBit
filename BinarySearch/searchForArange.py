class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
    	start = 0
    	end = len(A) - 1
    	arr = [-1, -1]
    	while start <= end:
    		mid = start + (end - start)//2
    		if A[mid] == B and (mid == 0 or A[mid - 1] < B):
    			arr[0] = mid
    			break
    		elif A[mid] == B and A[mid - 1] >= B:
    			end = mid - 1
    		elif A[mid] > B:
    			end = mid - 1
    		else:
    			start = mid + 1
    	start = 0
    	end = len(A) - 1
    	while start <= end:
    		mid = start + (end - start)//2
    		print(mid)
    		if A[mid] == B and (mid == len(A) -1 or A[mid + 1] > B):
    			arr[1] = mid
    			break
    		elif A[mid] == B and A[mid + 1] <= B:
    			start = mid + 1
    		elif A[mid] > B:
    			end = mid - 1
    		else:
    			start = mid + 1
    	return arr
sol = Solution()
print(sol.searchRange([1], 3))