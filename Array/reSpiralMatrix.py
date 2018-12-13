class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def spiral(self, A):
    	start_columb = 0
    	start_row = 0
    	end_columb = len(A)
    	end_row = len(A)
    	while start_columb < end_columb and start_row < end_columb:
    		for i in range(start_columb, end_columb):
    			print(A[start_row][i])
    			#print("ss1")
    		for j in range(start_row+1, end_row):
    			print(A[j][end_columb-1])
    			#print("ss2")
    		for i in range(end_columb-2, start_columb, -1):
    			print(A[end_row-1][i])
    			#print("ss3")
    		for j in range(end_row-1, start_row, -1):
    			print(A[j][start_columb])
    			#print("ss4")
    		start_columb += 1
    		start_row += 1
    		end_columb -= 1
    		end_row -= 1
sol = Solution()
print(sol.spiral([[1]]))
print(sol.spiral([[1, 2], [3, 4]]))
print(sol.spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(sol.spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]))
