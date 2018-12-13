class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		i = 0 
		j = 0
		while i < len(A) and j < len(A):
			if A[j] - A[i] == B and i != j:
				return 1
			elif A[j] - A[i] < B:
				j += 1
			elif A[j] - A[i] > B:
				i += 1
			else:
				j += 1
		return 0
sol = Solution()
print(sol.diffPossible([0],0))