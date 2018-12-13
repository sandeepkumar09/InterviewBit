class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
    	num = A.split(' ')
    	print(num)
    	for i in range(len(num)):
    		if num[i] != '':
    			return int(num[i])
    	return 0
sol = Solution()
print(sol.atoi('  9 256'))