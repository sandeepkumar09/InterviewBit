class Solution:
	# @param A : list of integers
	# @return an integer
	def nTriang(self, A):
		A.sort()
		count = 0
		for i in range(len(A)-2):
			k = i+2
			for j in range(i+1, len(A)):
				while k < len(A) and A[i] + A[j] > A[k]:
					k += 1
				count += k-j-1
		return count 