class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
    	val = 1
    	for i in range(len(A)-1 , -1, -1):
    		val = val + A[i]
    		borrow = int(val/10)
    		if borrow == 0:
    			A[i] = val
    			break
    		else:
    			A[i] = val % 10
    			val = borrow
    	A = [borrow] + A
    	while A[0] == 0:
    		del A[0]
    	return A
        # A[-1] = A[-1] + 1
        # length_A = len(A)
        # count = 0
        # # clearing the 0 from MSB
        # for i in range(length_A):
        # 	if A[i] == 0:
        # 		count += 1
        # 	else:
        # 		break
        # A = A[count:]
        # if length_A == 1 and A[-1] == 10:
        # 	A = [1,0]
        # 	print(A)
        # 	return  A
        # flag = False
        # if A[-1] == 10:
        #     A[-1] = 0
        #     for i in range(length_A-2 , -1, -1):
        #     	print("fff")
        #         if A[i] == 9:
        #             flag = True
        #             A[i] = 0
        #         else:
        #             flag = False
        #             A[i] = A[i] + 1
        #             break
        # if flag == True:
        #     A = [1] + A
        print(A)
        return A
sol = Solution()
print(sol.plusOne([9]))