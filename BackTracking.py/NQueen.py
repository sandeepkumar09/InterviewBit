class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        self.ans = []
        self.arr = [['.' for i in range(A)] for j in range(A)]
        self.helper(self.arr, 0, A)
        # for i in range(A):
        #     self.arr = [['.' for i in range(A)] for j in range(A)]
        #     self.arr[i][0] = 'Q'
        #     self.helper(self.arr, 1, A)
        return self.ans
    def isSafe(self, arr, row, col, N):
        for i in range(col):
            if arr[row][i] == 'Q':
                return False
        for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
            if arr[i][j] == 'Q':
                return False
        for i,j in zip(range(row, N, 1), range(col, -1, -1)):
            if arr[i][j] == 'Q':
                return False
        return True
    def helper(self, arr, col, N):
    	if col >= N:
    		temp = []
    		for i in arr:
    			temp.append(''.join(i))
    		self.ans.append(temp)
    	for i in range(N):
        	if self.isSafe(arr, i, col, N):
        		arr[i][col] = 'Q'
        		self.helper(arr, col+1, N)
        		arr[i][col] = '.'
sol = Solution()
print(sol.solveNQueens(5))
#print('[....Q ..Q.. Q.... ...Q. .Q... ] [....Q .Q... ...Q. Q.... ..Q.. ] [...Q. .Q... ....Q ..Q.. Q.... ] [...Q. Q.... ..Q.. ....Q .Q... ] [..Q.. ....Q .Q... ...Q. Q.... ] [..Q.. Q.... ...Q. .Q... ....Q ] [.Q... ....Q ..Q.. Q.... ...Q. ] [.Q... ...Q. Q.... ..Q.. ....Q ] [Q.... ...Q. .Q... ....Q ..Q.. ] [Q.... ..Q.. ....Q .Q... ...Q. ]')
# [....Q ..Q.. Q.... ...Q. .Q... ] [....Q .Q... ...Q. Q.... ..Q.. ] [...Q. .Q... ....Q ..Q.. Q.... ] [...Q. Q.... ..Q.. ....Q .Q... ] [..Q.. ....Q .Q... ...Q. Q.... ] [..Q.. Q.... ...Q. .Q... ....Q ] [.Q... ....Q ..Q.. Q.... ...Q. ] [.Q... ...Q. Q.... ..Q.. ....Q ] [Q.... ...Q. .Q... ....Q ..Q.. ] [Q.... ..Q.. ....Q .Q... ...Q. ]
