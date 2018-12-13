class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):
		length = len(A)
		k = 0
		i = 0
		while (i < (length-k)//2 ):
			if A[i] != A[len(A) - i - 1 - k]:
				i = -1
				k += 1
			i += 1
		return k
sol = Solution()
print(sol.solve('AB'))