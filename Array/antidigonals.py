class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        B = []
        # for k in range(2*len(A)-1):
        #     row = []
        #     for i in range(len(A)):
        #         for j in range(len(A)):
        #             if i+j == k:
        #                 #print(k,"KK")
        #                 row.append(A[i][j])
        #                 #print(row)
        k = 0
        di = 2*(len(A)-1)+1
        for i in range(len(A)):
        	for j in range(len(A)):
        		row = []
        		if i+j == k:
        			head = i; tail = j
        			while(head <len(A) and tail >=0):
        				row.append(A[head][tail])
        				head += 1
        				tail -= 1
        			if k < di:
        				B.append(row)
        				k += 1
        			else:
        				return B	
        return B
sol = Solution()
print(sol.diagonal([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]))
