class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
    	preCommonString = A[0]
    	for i in range(1,len(A)):
    		commonString = ''
    		newString = A[i]
    		length = min(len(newString), len(preCommonString))
    		for j in range(length):
    			if preCommonString[j] == newString[j]:
    				commonString += commonString.join(newString[j])
    			else:
    				break
    		preCommonString = commonString
    	return preCommonString
sol = Solution()
print(sol.longestCommonPrefix([ "abcdefgh", "aefghijk", "abcefgh"]))
print(sol.longestCommonPrefix( [ "abcd", "abde", "abcf" ]))