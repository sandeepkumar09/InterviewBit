class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        roman = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        # The last letter always gets added
        _sum = roman[A[-1]]
        print(A[:-1])
        print(A[1:])
        # Iterate over A in pairs of two
        for x, y in zip(A[:-1], A[1:]):
            current, _next = roman[x], roman[y]
            # If pair is like IV
            if current < _next:
                _sum -= current
            # Else if like VI
            else:
                _sum += current
        return _sum
sol = Solution()
print(sol.romanToInt('CXXXX'))