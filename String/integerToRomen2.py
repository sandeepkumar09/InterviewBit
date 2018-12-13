class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
    	intToRoman = ((1000, 'M'),
                        (900, 'CM'),
                        (500, 'D'),
                        (400, 'CD'),
                        (100, 'C'),
                        (90, 'XC'),
                        (50, 'L'),
                        (40, 'XL'),
                        (10, 'X'),
                        (9, 'IX'),
                        (5, 'V'),
                        (4, 'IV'),
                        (1, 'I'))
    	result = []
    	for val, char in intToRoman:
    		if A == 0:
    			break
    		while val <= A:
    			A -= val
    			result.append(char)
    	return  ''.join(result)
sol = Solution()
print(sol.intToRoman(3222))