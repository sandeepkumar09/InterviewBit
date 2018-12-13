import heapq
class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
		count_choc = 0
		B = [i*(-1) for i in B]
		minHeap = [i for i in B]
		heapq.heapify(minHeap)
		for i in range(A):
			count_choc += minHeap[0]
			heapq.heapreplace(minHeap,(-1)*(minHeap[0]*(-1)//2))
		return (-1*count_choc % ((10**9) + 7)) 


sol = Solution()
print(sol.nchoc(3, [6,5]))

