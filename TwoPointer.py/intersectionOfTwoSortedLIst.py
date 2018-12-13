class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	def intersect(self, A, B):
		i, j = 0, 0
		intersection = []
		while True:
			if i >= len(A) or j >= len(B):
				break
			if A[i] == B[j]:
				intersection.append(A[i])
				i += 1
				j += 1
			elif A[i] < B[j]:
				i += 1
			else:
				j += 1
		return intersection
sol = Solution()
print(sol.intersect([],[]))