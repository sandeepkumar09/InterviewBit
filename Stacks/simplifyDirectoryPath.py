class Solution:
	# @param A : string
	# @return a strings
	def simplifyPath(self, A):
		entries = A.split('/')
		newPath = []
		for entry in entries:
			if entry == '..':
				if newPath:
					newPath.pop()
			elif entry != '.':
				newPath.append(entry)
		newPath = [i for i in newPath if i]
		return '/'+'/'.join(newPath)

sol = Solution()
print(sol.simplifyPath("/a/./b/../../c/"))