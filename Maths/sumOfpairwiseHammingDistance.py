class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        flag, n, ans = 1, len(A), 0

        for i in range(32):
            cnt = 0
            for a in A:
                cnt += (a & flag) > 0

            ans = (ans + cnt * (n - cnt)) % 1000000007

            flag <<= 1

        return (ans * 2) % 1000000007
