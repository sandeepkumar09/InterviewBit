class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        head, tail = 1 << 31, 1

        for i in range(16):
            not_same = int(A & head > 0) ^ int(A & tail > 0)

            if not_same:
                A = A ^ tail ^ head

            head >>= 1
            tail <<= 1
        return A