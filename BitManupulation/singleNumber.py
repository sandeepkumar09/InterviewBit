class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
		num = 0
		for i in range(len(A)):
			num ^= A[i]
		return num
sol = Solution()
print(sol.singleNumber([1,2,3,1,3]))