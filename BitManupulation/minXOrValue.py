import sys
class Solution:
	# @param A : list of integers
	# @return an integer
	def findMinXor(self, A):
		A.sort()
		minXor =  int(sys.float_info.max)
		val = 0
		for i in range(len(A)-1):
			val = A[i] ^ A[i + 1];
			minXor = min(minXor, val);
		return minXor
sol = Solution()
print(sol.findMinXor([0 ,4 ,7 ,9 ]))