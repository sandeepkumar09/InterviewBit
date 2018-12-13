class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def gcd(self, A, B):
        if A < B:
            A, B = B, A
        if B == 0:
            return 1
        while True:
            reminder = A % B
            if reminder == 0:
                return B
            A = B
            B = reminder
        return 1

    def maxPoints(self, A, B):
        if len(A) == 0:
            return 0
        hashmap = {}
        sign = ''
        max_ = 1
        for i in range(len(A)):
            x1, y1 = A[i], B[i]
            for j in range(i+1, len(A)):
                x2, y2 = A[j], B[j]
                if x1 - x2 == 0:
                    slop = 'k'
                elif y1 - y2 == 0:
                    slop = 0
                else:
                    gcd = self.gcd(abs(y1 - y2), abs(x1 - x2))
                    Y = (y1 - y2) // gcd
                    X = (x1 - x2) // gcd
                    if (X < 0 and Y >= 0) or (X >= 0 and Y < 0):
                        sign = '-'
                    slop = sign + str(abs(Y)) + '/' + str(abs(X))
                # print('slop = ', slop, 'i =', i)
                if slop in hashmap:
                    if hashmap[slop][1] == i:
                        hashmap[slop] = [hashmap[slop][0] + 1, hashmap[slop][1]]
                else:
                    hashmap[slop] = [2, i]
                    # print(i)
        print(hashmap)
        for i in hashmap.values():
            max_ = max(i[0], max_)
        return max_


sol = Solution()
c = list(str(-4 - 17 - 5 - 18 10 12 - 16 - 18 8 - 2 0 - 7 13 14 2 17 20 - 15 9 - 17 - 12 2 17 - 13 16 - 5 - 3 20 - 17 - 11 - 2 5 1 - 18 - 11 - 18 11 14 - 5 18 12 - 1 - 14 3 - 8 8 - 10 13 - 2 13 11 6 4 - 3 19 - 1 6 17 - 5 14 - 4 0 13 8 - 10 16 - 6 - 17 1 10 - 19 20 - 18 - 2 10 18 5 - 20 - 13 - 5 - 13 0 - 2 17 1 5 - 15 - 1 - 10 8 13 - 6 - 4 - 20 - 19 - 11 6 13 18 - 20 - 14 14 6 - 10 6 - 15 14 9 - 5 - 7 17 8 2 16 14 0 10 - 10 - 6 2 - 15 5 - 16 13 - 15 - 18 19 7 14 - 18 2 0 - 14 9 5 2 16 - 15 11 19 18 - 4 5 17 - 8 3 20 - 8 19 - 10 - 7 15 5 9 11 - 14 11 - 7 0 - 4 5 11 20 13 - 11 - 12 - 5 1 - 11 - 9 - 14 - 16 15 - 10 - 9 - 12 - 1 - 11 0 10 - 16 - 15 - 6 - 17 - 7 - 15 - 16 - 19 4 - 12 6 5 - 1 13 - 18 - 7))
print(c)
A = [c[i] for i in range(len(c)) if i % 2 == 0]
B = [c[i] for i in range(len(c)) if i % 2 != 0]
print(sol.maxPoints(A, B))
