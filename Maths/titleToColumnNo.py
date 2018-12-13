class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
    	title = []
    	title_s = ''
    	alphabate = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    	while A:
    		#print(A%26)
    		#print(int(A%26)-1)
    		title.append(alphabate[int(A%26)-1])
    		A = A-1
    		A /= 26
    	for i in reversed(title):
    		title_s += str(i)
    	return title_s
sol = Solution()
#print(sol.convertToTitle(703))
print(sol.convertToTitle(468096))