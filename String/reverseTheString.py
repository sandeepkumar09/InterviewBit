class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
    	arr = A.split(' ')
    	A = ''
    	print(arr)
    	for i, ele in enumerate(reversed(arr)):
    		print(i)
    		if i == len(arr)-1:
    			A = A + ele
    			return A
    		A = A + ele +' '
    	return A
sol = Solution()
print(sol.reverseWords("l np dtejcxftenksppymy scbdql xdnzwj l gellcrpyhwqxwlrthbrjqochekqqtf cmc pf lnzu"))