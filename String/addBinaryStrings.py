class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
		carry = 0
		ans = []
		if len(A) < len(B):
			A, B = B, A
		for i in range(len(B)):
			if B[len(B)-1-i] == '1' and carry == 1:
				if A[len(A)-1-i] == '1':
					ans.append(1)
				else:
					ans.append(0)
				carry = 1
			elif B[len(B)-1-i] == '1' and carry == 0:
				if A[len(A)-1-i] == '1':
					ans.append(0)
					carry = 1
				else:
					ans.append(1)
			elif B[len(B)-1-i] == '0' and carry == 1:
				if A[len(A)-1-i] == '1':
					ans.append(0)
					carry = 1
				else:
					ans.append(1)
					carry = 0
			else:
				ans.append(int(A[len(A)-1-i]))
		for j in range(len(A)-len(B)):
			if carry == 1:
				if A[len(A)-len(B)-j-1] == '1':
					ans.append(0)
				else:
					ans.append(1)
					carry = 0
			else:
				ans.append(int(A[len(A)-len(B)-j-1]))
		if carry == 1:
			ans.append(1)
		return ''.join(str(i) for i in reversed(ans))
sol = Solution()
print(sol.addBinary("01", "0"))