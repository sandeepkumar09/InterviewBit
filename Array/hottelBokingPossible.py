class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
    	arrive.sort()
    	depart.sort()
    	start = arrive[0]
    	end = depart[-1]
    	A , D = 0, 0
    	for i in range(start, end+1):
    		while(D < len(depart) and (i == depart[D])):
    			K += 1
    			D += 1
    		while(A < len(arrive) and (i == arrive[A])):
    			if K > 0:
    				K -= 1
    			else:
    				return 0
    			A += 1
    	return 1