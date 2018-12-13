class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        start = min(A)
        end = max(A)
        while start < end:
            mid = start + (end-start)//2
            ans = self.binarySearch(A, mid)
            if ans == B and (mid in A):
                return mid
            elif ans < B:
                start = mid+1
            else:
                end = mid
           ## print(ans, mid)
        return start
    def binarySearch(self, A, Mid):
        total = 0
        for i in A:
            if i <= Mid:
                total += 1
        return total
sol = Solution()
p
print(sol.kthsmallest([ 74, 90, 85, 58, 69, 77, 90, 85, 18, 36 ], 1))
a = [ 25, 87, 98, 30, 41, 94, 89, 49, 59, 25, 2, 24, 93, 19, 88, 87, 72, 36, 44, 24, 68, 16, 7, 46, 39, 90 ]
a.sort()
print(a)
print(sol.kthsmallest([ 25, 87, 98, 30, 41, 94, 89, 49, 59, 25, 2, 24, 93, 19, 88, 87, 72, 36, 44, 24, 68, 16, 7, 46, 39, 90 ],7))