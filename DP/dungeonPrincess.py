class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        if not A:
            return 0
        n = len(A)
        m = len(A[0])
        self.health = 0
        self.visited = [[0 for i in range(m)] for j in range(n)]
        self.dp = [[0 for i in range(m)] for j in range(n)]
        a = self.Pathsum(n-1, m-1, n, m, A, self.visited, self.dp, 0)
        print(self.dp)
        return (self.dp[0][0] * (-1))+1
    def Pathsum(self, i, j ,n, m, arr, visited, dp, health):
        if visited[i][j] == 1:
            return dp[i][j]
        visited[i][j] = 1
        if i == 0 and j == 0:
            #return arr[i][j]
            if health+arr[i][j] > 0:
                health = 0
            else:
                health = health+arr[i][j]
            dp[i][j] = health
        elif i == 0:
            if health+arr[i][j] > 0:
                health = 0
            else:
                health = health+arr[i][j]
            #return arr[i][j]+self.Pathsum(i, j+1, n, m, arr, visited, dp)
            dp[i][j] = max(health, 0 ,health-self.Pathsum(i, j-1, n, m, arr, visited, dp, health))
        elif j == 0:
            if health+arr[i][j] > 0:
                health = 0
            else:
                health = health+arr[i][j]
            #return arr[i][j]+self.Pathsum(i+1,j, n, m, arr, visited, dp)
            dp[i][j] = min(health, 0, health+self.Pathsum(i-1,j, n, m, arr, visited, dp, health))
        else:
            #return arr[i][j]+min(self.Pathsum(i+1, j, n, m, arr, visited, dp), self.Pathsum(i, j+1, n, m, arr, visited, dp))
            if health+arr[i][j] > 0:
                health = 0
            else:
                health = health+arr[i][j]
            dp[i][j] = max(health,0,health+min(self.Pathsum(i-1, j, n, m, arr, visited, dp, health), self.Pathsum(i, j-1, n, m, arr, visited, dp, health)))
        return dp[i][j]


sol = Solution()
print(sol.calculateMinimumHP([[2,-3,3],[-5,-10,1],[10,30,-5]]))
print(sol.calculateMinimumHP([[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]))
print(sol.calculateMinimumHP([
  [6, -15, -35, -6, -3, 1, -11, -81, -82, 2, -88, -43, -58, -35, -38, 3, -57, -46, -60, 5],
  [-75, -24, -60, -36, -31, -61, -46, -67, -92, -97, -26, -97, -28, -67, -35, -55, -33, -89, 10, -63],
  [-98, -75, -2, 7, -7, -65, -24, -45, -70, -85, -41, -12, -50, -100, -45, -85, -89, 9, -28, -41],
  [-3, -67, -93, 0, -39, -17, -58, -9, -62, -20, -63, -57, -13, -23, -86, -90, -64, -52, -45, 4],
  [-81, -42, -13, -29, -69, -5, -50, -71, -96, -19, -10, -60, -41, -42, -26, -28, -97, -45, -51, -14],
  [-69, -80, -61, 6, -91, -27, -94, -80, -2, -44, -98, -93, -91, -64, -39, -64, -56, -79, -51, -2],
  [3, -45, -71, -100, -51, -23, -31, -73, -96, -66, -37, 1, -59, -41, 2, -92, -29, -83, 4, -85],
  [-47, -23, -20, -3, -66, -26, -9, -100, -34, -17, -74, -59, 1, -73, -37, -80, -67, -99, -86, -31],
  [-26, -19, -56, 6, -15, -65, -83, -29, -77, -21, -23, -5, -67, 6, -44, -78, -34, -14, -49, -34],
  [-17, -51, -36, -26, -67, -33, -18, -32, -5, -22, -91, -13, -76, -26, -44, -90, -20, 9, -59, -22],
  [-4, -1, -42, -5, -20, 0, -90, -89, -59, -95, -63, -27, -29, 3, -64, -67, 2, -19, 1, -40],
  [-17, -80, -29, -88, -60, -22, 4, -53, -88, -57, -44, -59, -63, -1, -78, -85, -27, -44, -28, -30],
  [-32, -33, -47, -40, -75, -76, -34, -5, 10, -19, -73, -31, -13, -26, -77, -73, -72, -74, -68, -41],
  [-74, 2, -93, -4, -20, -25, -81, -55, -71, -21, -91, -71, -55, -63, -7, -43, -21, -7, -26, -62],
  [-68, 5, -79, -48, -16, -98, -50, -59, -84, -89, -46, -5, -96, -29, -33, -14, -83, -78, -94, -82],
  [-92, -78, -88, -26, -42, -78, -15, -6, -32, -45, -70, -29, -73, -32, -12, -48, -38, -79, -88, -76],
  [-41, 3, -94, -9, -15, -48, -53, -12, -80, -65, -7, -1, -75, -79, 6, -22, -90, -30, -65, -83],
  [-99, -52, -44, -53, -91, -6, -37, 4, -76, -64, 3, -27, -57, 8, 4, -90, -18, -34, 5, -3],
  [-60, -1, -5, -93, -15, -2, -96, -66, -36, -42, -1, -21, -10, -62, -47, -39, -69, -49, -36, -51],
  [-57, -65, -12, -63, -91, -6, -39, -37, -53, -63, -76, -13, -93, -78, -30, -8, -54, -92, -52, -41]
]))