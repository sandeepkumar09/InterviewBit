class Solution:
	# @param A : integer
	# @return a strings
	def countAndSay(self, A):
		A = A - 1
		ans = '1'
		count = 0
		length = 1
		for j in range(A):
			B = ans
			ans = ''
			count = 0
			for i in range(1,length):
				if B[i] == B[i-1]:
					count += 1
				else:
					print(i)
					ans += ans.join(str(count + 1))
					ans += ans.join(str(B[i-1]))
					count = 0
			ans += ans.join(str(count + 1))
			ans += ans.join(str(B[-1]))
			length = len(ans)
		return ans
sol = Solution()
print(sol.countAndSay(3))