class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
    	j = 0
    	length = 0
    	for i in range(len(A)):
    		#print (B[j])
    		if A[i] == B[j]:
    			length += 1
    			j += 1
    			#print(length)
    			if length == len(B):
    				return i - len(B) + 1
    		else:
    			j = 0
    			length = 0
    			if A[i] == B[j]:
    				length += 1
    				j += 1
    	return -1
sol = Solution()
print(sol.strStr( "bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba", "babaaa"))
print('hayStack'.find('S'))
print('bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba'.find('babaaa'))
print('"aabaaaababaabbbabbabbbaabababaaaaaababaaabbabbabbabbaaaabbbbbbaabbabbbbbabababbaaabbaabbbababbb"'.find('bba'))
print(len('bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbab'))