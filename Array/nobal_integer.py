class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
    	# A.sort()
    	# print(A)
    	# if A[len(A)-1] == 0:
    	# 	print(1,"jjj")
    	# 	return 1
    	# for i in range(len(A)-1):
    	# 	current_integer = A[i]
    	# 	if current_integer != A[i+1]:
    	# 		print(i+1,"jjjjis")
    	# 		if current_integer == len(A)-i - 1:
    	# 			print(current_integer, len(A), i-1)
    	# 			print(1)
    	# 			return 1
    	# return -1
        A.sort()
        # if A[-1] == 0:
        #     return 1
        for i,integer in enumerate(A):
            current_integer = integer
            if (current_integer == len(A)-i-1) and i+1 < len(A):
            	next_integer = A[i+1]
            	if current_integer != next_integer:
            		return 1
        return -1
print("na")
sol = Solution()
print(sol.solve([ -4, 7, 5, 3, 5, -4, 2, -1, -9, -8, -3, 0, 9, -7]))


