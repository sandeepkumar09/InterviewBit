class Solution:
	# @param A : list of integers
	# @return an integer
	def maxSpecialProduct(self, A):
		maxSpecialProduct = 0
		leftSpecialValue = 0
		rightSpecialValue = 0
		constant = 1000000007
		for i in range(1,len(A)):
			for j in range(i-1,-1,-1):
				if A[i] < A[j]:
					leftSpecialValue = j % constant
					break
			for k in range(i+1, len(A)):
				if A[i] < A[k]:
					rightSpecialValue = k % constant
					break
			maxSpecialProduct = max(maxSpecialProduct, (leftSpecialValue*rightSpecialValue) % constant)
			leftSpecialValue, rightSpecialValue = 0, 0
		return maxSpecialProduct