class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        self.arr = A
        self.helper(self.arr, 0, 0)
        return self.arr
    def canPut(self, board, char, row, col):
        for i in range(0,9):
            if board[row][i] == char:
                return False
            if board[i][col] == char:
                return False
        rowGroup = (row//3) * 3
        colGroup = (col//3) * 3
        for i in range(rowGroup, rowGroup+3):
            for j in range(colGroup, colGroup+3):
                if board[i][j] == char:
                    return False
        return True
    def helper(self, arr, row, col):
        if row == 9:
            return Ture
        if col == 8:
            row += 1
            nextCol = col+1
        else:
            nextRow = row
            nextCol = col
        if arr[row][col] != '.':
            return self.helper(arr, nextRow, nextCol)
        for c in range(1,10):
            if self.canPut(arr, str(c), row, col):
                arr[row][col] = '.'
                if self.helper(arr, nextRow, nextCol):
                    return True
                arr[row][col] = '.'
        return False


sol = Solution()
print(sol.solveSudoku([[5,3,0,0,7,0,0,0,0], [6,0,0,1,9,5,0,0,0], [0,9,8,0,0,0,0,6,0], [8,0,0,0,6,0,0,0,3], [4,0,0,8,0,3,0,0,1], [7,0,0,0,2,0,0,0,6], [0,6,0,0,0,0,2,8,0], [0,0,0,4,1,9,0,0,5], [0,0,0,0,8,0,0,7,9]]))
