class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        size = float(len(A)/3)
        print(size)
        A.sort()
        count = 0
        if len(A) == 1:
        	return A[0]
        for i in range(len(A)-1):
            num = A[i]
            if num == A[i+1]:
                count += 1
            else:
                count = 0
            print(count)
            if count + 1 > size:
            	return num
        return -1
sol = Solution()
print(sol.repeatedNumber([1000441, 1000441, 1000994 ]))