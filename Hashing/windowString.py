import sys
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
    	if len(A) < len(B):
    		return ''
    	p1 , p2 = 0, 0
    	min_window = sys.maxsize
    	hashmap = {}
    	hashmap1 = {}
    	hashmap2 = {}
    	for i in range(len(B)):
    		if B[i] in hashmap1:
    			hashmap1[B[i]] += 1
    			hashmap[B[i]] += 1
    		else:
    			hashmap1[B[i]] = 1
    			hashmap[B[i]] = 1
    	print(hashmap)
    	for p2 in range(len(A)):
    		print(hashmap1)
    		print(hashmap2)
    		print(p2, A[p2])
    		if A[p2] in hashmap2:
    			hashmap2[A[p2]] += 1
    			if A[p2] in hashmap1:
    				if hashmap1[A[p2]] == 1:
    					hashmap1.pop(A[p2])
    				else:
    					hashmap1[A[p2]] -= 1
    		elif A[p2] in hashmap1:
    			hashmap2[A[p2]] = 1
    			if hashmap1[A[p2]] == 1:
    				hashmap1.pop(A[p2])
    			else:
    				hashmap1[A[p2]] -= 1
    		if not hashmap1:
    			print('in')
    			print(p2)
    			while p1 <= p2:
    				print(p1,A[p1])
    				if A[p1] in hashmap2:
    					print(hashmap)
    					if hashmap2[A[p1]] == hashmap[A[p1]]:
    						hashmap2.pop(A[p1])
    						if min_window > p2 - p1 + 1:
    							print('d', p2 - p1 + 1)
    							min_window = p2 - p1 +1
    							s = p1
    							e = p2
    						hashmap1[A[p1]] = 1
    						p1 = p1 + 1
    						break
    					else:
    						hashmap2[A[p1]] -= 1
    				p1 += 1
    	else:
    		if min_window == sys.maxsize:
    			print('dd')
    			return ''
    	return A[s : e+1]


sol = Solution()
print(sol.minWindow('AAA', 'AA'))
