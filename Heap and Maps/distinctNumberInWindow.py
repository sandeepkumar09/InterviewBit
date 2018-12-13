class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
		if B > len(A):
			return []
		res = []
		hashmap = {}
		for i in range(B):
			hashmap[A[i]] = i
		res.append(len(hashmap))
		for i in range(B, len(A)):
			print(hashmap)
			if A[i-B] in hashmap and hashmap[A[i-B]] == i-B:
				hashmap.pop(A[i-B])
			hashmap[A[i]] = i
			res.append(len(hashmap))
		return res
sol = Solution()
print(sol.dNums([ 2, 7, 7, 81, 81 ], 1))