class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
		increasing, area, i = [], 0, 0
		while i <= len(A):
			if not increasing or (i < len(A) and A[i] >= A[increasing[-1]]):
				increasing.append(i)
				i += 1
			else:
				last = increasing.pop()
				if not increasing:
					area = max(area, A[last] * i)
				else:
					area = max(area, A[last]*(i - increasing[-1]-1))
		return area