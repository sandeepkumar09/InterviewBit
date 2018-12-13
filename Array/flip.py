class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
    	length_A =len(A)
    	B = ''
    	for j in range(length_A):
    		B = B + '1'
    	if A == str(B):
    		return []
    	B = list(A)
    	count = 0
    	max_0 = 0
    	max_run = -1
    	start = 1
    	end = 0
    	for i in range(len(B)):
    		if count < 0:
    			count = 0
    			start = i+1
    		if B[i] == "0":
    			count += 1
    		else:
    			count -= 1
    			print("de",count)
    		if count >0:
    			end = i+1
    		if max_0 < count:
    			max_0 = count
    			s = start
    			e = end
    		max_0 = max(max_0, count)
    	print([s,e])
    	return [s,e]
sol = Solution()
sol.flip("010")
