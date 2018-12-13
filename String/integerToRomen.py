class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
    	romanNumber = ''
    	if A == 0:
    		return ''
    	for i in range(A // 1000):
    		romanNumber += romanNumber.join('M')
    	A = A % 1000
    	for i in range(len(str(A))):
    		if A >= 900:
    			romanNumber += 'CM'
    			A = A - 900
    		elif A >= 800:
    			romanNumber += 'DCCC'
    			A -= 800
    		elif A >= 700:
    			romanNumber += 'DCC'
    			A -= 700
    		elif A >= 600:
    			romanNumber += 'DC'
    			A -= 600
    		elif A >= 500:
    			romanNumber += 'D'
    			A -= 500
    		elif A >= 400:
    			romanNumber += 'CD'
    			A -= 400
    		elif A >= 300:
    			romanNumber += 'CCC'
    			A -= 300
    		elif A >= 200:
    			romanNumber += 'CC'
    			A -= 200
    		elif A >= 100:
    			romanNumber += 'C'
    			A -= 100
    		elif A >= 90:
    			romanNumber += 'XC'
    			A -= 90
    		elif A >= 80:
    			romanNumber += 'LXXX'
    			A -= 80
    		elif A >= 70:
    			romanNumber += 'LXX'
    			A -= 70
    		elif A >= 60:
    			romanNumber += 'LX'
    			A -= 60
    		elif A >= 50:
    			romanNumber += 'L'
    			A -= 50
    		elif A >= 40:
    			romanNumber += 'XL'
    			A -= 40
    		elif A >= 30:
    			romanNumber += 'XXX'
    			A -= 30
    		elif A >= 20:
    			romanNumber += 'XX'
    			A -= 20
    		elif A >= 10:
    			romanNumber += 'X'
    			A -= 10
    		elif A >= 9:
    			romanNumber += 'IX'
    			A -= 9
    		elif A >= 8:
    			romanNumber += 'VIII'
    			A -= 8
    		elif A >= 7:
    			romanNumber += 'VII'
    			A -= 7
    		elif A >= 6:
    			romanNumber += 'VI'
    			A -= 6
    		elif A >= 5:
    			romanNumber += 'V'
    			A -= 5
    		elif A >= 4:
    			romanNumber += 'IV'
    			A -= 4
    		elif A >= 3:
    			romanNumber += 'III'
    			A -= 3
    		elif A >= 2:
    			romanNumber += 'II'
    			A -= 2
    		elif A >= 1:
    			romanNumber += 'I'
    			A -= 1
    		elif A == 0:
    			return romanNumber
    		else:
    			pass
    	#print(romanNumber)
    	#print(romanNumber)
    	return romanNumber
sol = Solution()
print(sol.intToRoman(101))