class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
    	startR = 0
    	startC = 0
    	endR = len(A) - 1
    	endC = len(A[0]) - 1
    	row = 0
    	while startR <= endR:
    		midR = startR + (endR - startR)//2
    		#midC = startC + (endC - startC)//2
    		if (A[midR][endC]) >= B and A[midR - 1][endC] < B:
    			row = midR
    			break
    		elif A[midR ][endC] > B:
    			endR = midR - 1
    			#endC = midC - 1
    		else:
    			startR = midR + 1
    			#endC = midC + 1
    	while startC <= endC:
    		midC = startC + (endC - startC)//2
    		if A[row][midC] == B:
    			return 1
    		elif A[row][midC] > B:
    			endC = midC - 1
    		else:
    			startC = midC + 1
    	return 0
sol = Solution()
print(sol.searchMatrix([  [1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50] ], 4))