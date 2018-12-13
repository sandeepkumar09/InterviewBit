class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
    	if len(A) < B:
    		return -1
    	start = max(A)
    	end = sum(A)
    	while start < end:
    		mid = start + (end - start)//2
    		requiredDistribution = self.BookDistribution(A, mid)
    		if requiredDistribution <= B:
    			end = mid
    		else:
    			start = mid + 1
    		print("start" , start, "mid" , mid, "end" , end )
    	return start
    def BookDistribution(self, arr, maxPage):
    	numStudent = 1
    	pageAssigned = 0
    	for i in arr:
    		pageAssigned += i
    		if pageAssigned > maxPage:
    			pageAssigned = i
    			numStudent += 1
    	return numStudent
sol = Solution()
print(sol.books([12,12,1], 2))