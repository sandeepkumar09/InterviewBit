class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
    	ip = []
    	arr = []
    	num = ''
    	for i in reversed(A):
    		count = 3
    		previousNum = num
    		num = i + num
    		print(num)
    		if int(num) > 255:
    			if count == 0:
    				ip.append(previousNum)
    			else:
    				ip.append('.'+PreviousNum)
    			num = ''
    			previousNum = ''
    			count -= 1
    	arr.append(ip)
    	ip = []
    	print(arr)
sol = Solution()
sol.restoreIpAddresses('123')