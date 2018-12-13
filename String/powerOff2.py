class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
    	if A == 1 or A == 0:
    		return 0
    	B = A -1
    	if A & B == 0:
    		return 1
    	else:
    		return 0
    	return 0
print(2**67)
print(3.2 > 3)
print(4/2)