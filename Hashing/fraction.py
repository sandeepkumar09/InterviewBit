class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):
        if A == 0:
            return '0'
        sign = ''
        if (A < 0 or B < 0) and (A >= 0 or B >= 0):
            sign = '-'
        if A < 0:
            A *= -1
        if B < 0:
            B *= -1
        denominator = B
        numerator = A
        while B % 2 == 0:
            B /= 2
        while B % 5 == 0:
            B /= 5
        if B == 1:
            if numerator % denominator == 0:
                return sign + str(numerator // denominator)
            # return sign + str(numerator / denominator)
        hashmap = {}
        riminder = A % denominator
        A = A - riminder
        ans = str(A // denominator)
        A = riminder
        fraction = []
        i = 0
        val = 0
        while True:
            if A in hashmap or A == 0:
                if A != 0:
                    val = hashmap[A]
                break
            hashmap[A] = i
            i += 1
            A = A * 10
            fraction.append(str(A // denominator))
            A = A % denominator
        if A != 0:
            fraction.insert(val, '(')
            fraction.append(')')
        return sign + ans + '.' + (''.join(fraction))


sol = Solution()
print(sol.fractionToDecimal(-1, -2147483648))
print(sol.fractionToDecimal(87, 22))
