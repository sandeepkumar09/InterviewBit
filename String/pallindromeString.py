import re
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
    	A = re.sub('[^A-z0-9]','', A)
    	print(A)
    	B = ''
    	for i in range(len(A)):
    		B += B.join(A[i].lower())
    	print(B)
    	for i in range(len(B)//2):
    		if B[i] != B[len(B) - 1 - i]:
    			return 0
    	return 1
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
