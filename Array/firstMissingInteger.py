class Solution:
	# @param A : list of integers
	# @return an integer
	def firstMissingPositive(self, A):
		A.sort()
		integer = 1
		for i in range(len(A)):
			if A[i] > 0:
				if integer != A[i]:
					return integer
				else:
					integer += 1
		return integer
sol = Solution()
print(sol.firstMissingPositive([1,2,0]))
