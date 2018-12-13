class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def multiply(self, A, B):
		num1, num2 = 0, 0
		_max = max(len(A), len(B))
		result = [0]*(len(A) + len(B))
		i_n1, in2 = 0, 0
		for i in reversed(A):
			carry = 0
			
sol = Solution()
print(sol.multiply('12', '10'))