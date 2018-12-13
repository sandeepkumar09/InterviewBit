class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
    	arr = A.split(' ')
    	print(arr)
    	for i in reversed(arr):
    		if i != '':
    			return len(i)
    	return 0
sol = Solution()
print(sol.lengthOfLastWord("Hello World "))