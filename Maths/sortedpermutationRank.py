class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
    	B = A.sort()
    	for i, element in enumerate(A):
    		B.find(element)
    		count += B.find(element)+ 
