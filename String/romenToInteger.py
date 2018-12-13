class Solution:
	# @param A : string
	# @return an integer
	def romanToInt(self, A):
		if len(A) == 0:
			return 0
		num = 0
		i = -1
		for i in range(len(A)-1):
			if A[i] == 'M':
				num += 1000
			elif A[i] == 'C' and (A[i+1] == 'M' or A[i+1] == 'D'):
				num -= 100
			elif A[i] == 'C':
				num += 100
			elif A[i] == 'D':
				num += 500
			elif A[i] == 'L' and (A[i+1] == 'M' or A[i+1] == 'D' or A[i+1] == 'C'):
				num -= 50
			elif A[i] == 'L':
				num += 50
			elif A[i] == 'X' and (A[i+1] == 'M' or A[i+1] == 'D' or A[i+1] == 'C' or A[i+1] == 'L'):
				num -= 10
			elif A[i] == 'X':
				num += 10
			elif A[i] == 'V' and (A[i+1] == 'M' or A[i+1] == 'D' or A[i+1] == 'C' or A[i+1] == 'L' or A[i+1] == 'X'):
				num -= 5
			elif A[i] == 'V':
				num += 5
			elif A[i] == 'I' and (A[i+1] == 'M' or A[i+1] == 'D' or A[i+1] == 'C' or A[i+1] == 'L' or A[i+1] == 'X' or A[i+1] == 'V'):
				num -= 1
			elif A[i] == 'I':
				num += 1
			else:
				num += 0
		if A[i+1] == 'M':
			num += 1000
		elif A[i+1] == 'D':
			num += 500
		elif A[i+1] == 'C':
			num += 100
		elif A[i+1] == 'L':
			num += 50
		elif A[i+1] == 'X':
			num += 10
		elif A[i+1] == 'V':
			num += 5
		elif A[i+1] == 'I':
			num += 1
		else:
			num += 0
		return num
sol = Solution()
print(sol.romanToInt('V'))