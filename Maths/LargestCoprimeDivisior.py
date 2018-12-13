class Solution:
    def gcd(self, A, B):
        while B:
            A, B = B, A % B
        return A
    def cpFact(self, A, B):
        while True:
            gcd = self.gcd(A, B)
            if gcd == 1:
                break
            A = A // gcd
        return A