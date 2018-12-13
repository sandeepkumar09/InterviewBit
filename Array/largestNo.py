def comparator(a, b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    return cmp(int(ba), int(ab))
class Solution:
	# @param A : tuple of integers
	# @return a strings

	def largestNumber(self, A):
		sorted_array = sorted(A,cmp = comparator)
		number = "".join([str(i) for i in sorted_array])
		return number
sol = Solution()
print(sol.largestNumber([2,1,82]))
